import os
import sys
import json
import shutil
import hashlib
import torch
import orjson
from tqdm import tqdm
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from globals import Global


class DocumentIngestor:
    def __init__(self, dataset_path, config_path='config/config.json'):
        self.dataset_path = dataset_path
        Global.init(config_path)

        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[INFO] Using device: {device}")

        self.embedding_batch_size = min(512, Global.config.get("EMBEDDING_BATCH_SIZE", 512))

        self.embedding_model = HuggingFaceEmbeddings(
                model_name=Global.config["HUGGINGFACE_MODEL"],
                model_kwargs={"device": device},
                encode_kwargs={
                    "batch_size": self.embedding_batch_size  # ✅ Only this
                }
            )

        self.vectorstore = Chroma(
            embedding_function=self.embedding_model,
            persist_directory=Global.config.get("CHROMA_PERSIST_DIR", "./chroma_db")
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Global.config["CHUNK_SIZE"],
            chunk_overlap=Global.config["CHUNK_OVERLAP"]
        )

        self.seen_hashes = self.load_hashes()

    def hash_doc(self, content, title=""):  
        return hashlib.md5((content + title).encode("utf-8")).hexdigest()

    def load_hashes(self, path=".seen_hashes.json"):
        if os.path.exists(path):
            with open(path, "r") as f:
                return set(json.load(f))
        return set()

    def save_hashes(self, path=".seen_hashes.json"):
        with open(path, "w") as f:
            json.dump(list(self.seen_hashes), f)

    def read_checkpoint(self, path=".ingest_checkpoint"):
        if os.path.exists(path):
            with open(path, "r") as f:
                return int(f.read().strip())
        return 0

    def write_checkpoint(self, line_number, path=".ingest_checkpoint"):
        with open(path, "w") as f:
            f.write(str(line_number))

    def ingest(self, batch_size=5000):
        buffer = []
        batch_number = 1
        total_ingested = 0

        start_line = self.read_checkpoint()
        with open(self.dataset_path, 'rb') as f:
            total_lines = sum(1 for _ in f)

        with open(self.dataset_path, 'rb') as f, tqdm(
            total=total_lines, desc="Ingesting", unit="lines", initial=start_line
        ) as pbar:
            for line_num, line in enumerate(f, start=1):
                if line_num <= start_line:
                    continue
                pbar.update(1)

                try:
                    record = orjson.loads(line)
                    if not record.get("abstract"):
                        continue
                    doc = Document(
                        page_content=record["abstract"],
                        metadata={
                            "title": record.get("title", ""),
                            "categories": record.get("categories", "")
                        }
                    )
                    buffer.append(doc)

                    if len(buffer) >= batch_size:
                        ingested_count = self._process_batch(buffer, batch_number)
                        total_ingested += ingested_count
                        self.write_checkpoint(line_num)
                        self.save_hashes()
                        print(f"📦 Batch #{batch_number} — {ingested_count} docs | Total: {total_ingested}")
                        buffer.clear()
                        batch_number += 1

                except Exception as e:
                    print(f"[Line {line_num}] Error: {e}")
                    continue

            if buffer:
                ingested_count = self._process_batch(buffer, batch_number)
                total_ingested += ingested_count
                self.write_checkpoint(line_num)
                self.save_hashes()
                print(f"📦 Final Batch #{batch_number} — {ingested_count} docs | Total: {total_ingested}")

    def _process_batch(self, docs, batch_number):
        all_docs = []
        for doc in docs:
            splits = self.text_splitter.split_documents([doc])
            for s in splits:
                doc_hash = self.hash_doc(s.page_content, s.metadata.get("title", ""))
                if doc_hash not in self.seen_hashes:
                    self.seen_hashes.add(doc_hash)
                    all_docs.append((s, doc_hash))

        if all_docs:
            split_docs, ids = zip(*all_docs)
            for i in range(0, len(split_docs), self.embedding_batch_size):
                chunk_docs = list(split_docs[i:i + self.embedding_batch_size])
                chunk_ids = list(ids[i:i + self.embedding_batch_size])
                try:
                    self.vectorstore.add_documents(chunk_docs, ids=chunk_ids)
                except Exception as e:
                    print(f"⚠️ Batch {batch_number}, chunk {i} failed: {e}")
                    if "batch size" in str(e).lower():
                        smaller_batch = max(1, self.embedding_batch_size // 2)
                        print(f"Retrying with smaller batch size: {smaller_batch}")
                        for j in range(0, len(chunk_docs), smaller_batch):
                            self.vectorstore.add_documents(
                                chunk_docs[j:j + smaller_batch],
                                ids=chunk_ids[j:j + smaller_batch]
                            )
            return len(split_docs)
        return 0


if __name__ == "__main__":
    dataset_path = "arxiv-metadata-oai-snapshot.json"

    if "--reset" in sys.argv:
        if os.path.exists(".ingest_checkpoint"):
            os.remove(".ingest_checkpoint")
        if os.path.exists(".seen_hashes.json"):
            os.remove(".seen_hashes.json")
        if os.path.exists('./chroma_db'):
            shutil.rmtree('./chroma_db')
        print("✅ Reset complete.")

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"❌ The dataset {dataset_path} does not exist.")

    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    ingestor = DocumentIngestor(dataset_path)
    ingestor.ingest(batch_size=4000)
