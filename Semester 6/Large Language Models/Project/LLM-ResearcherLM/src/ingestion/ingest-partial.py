# """
# Module: Document Ingestor
# """
# import os
# from langchain_community.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_elasticsearch import ElasticsearchStore
# from langchain_huggingface import HuggingFaceEmbeddings
# import matplotlib.pyplot as plt
# from sklearn.manifold import TSNE
# import numpy as np
# from globals import Global


# class DocumentIngestor:
#     """
#     Class: DocumentIngestor

#     A class to handle ingestion of documents from a text file.

#     Attributes:
#     - file_path
#     - embedding_model
#     - vectorstore

#     Methods:
#     - __init__(self, file_path, config_path='config/config.json')
#     - load_documents(self)
#     - split_documents(self, docs)
#     - generate_embeddings(self, splits)
#     - add_embeddings_to_vectorstore(self, embeddings)
#     - plot_embeddings(self, embeddings)
#     - ingest(self)
#     """

#     def __init__(self, file_path, config_path='config/config.json'):
#         """
#         Args:
#         - file_path (str)
#         - config_path (str, optional)
#         """
#         self.file_path = file_path
#         Global.init(config_path)
#         self.embedding_model = HuggingFaceEmbeddings(
#             model_name=Global.config["HUGGINGFACE_MODEL"])
#         self.vectorstore = ElasticsearchStore(      # Change to VectorStore
#             embedding=self.embedding_model,
#             index_name=Global.config["INDEX_NAME"],
#             es_url=Global.config["ELASTICSEARCH_URL"]
#         )

#     def load_documents(self):
#         """
#         Load documents from the specified file path.
#         Returns:
#         - list: List of loaded documents.
#         """
#         loader = TextLoader(self.file_path)
#         return loader.load()

#     def split_documents(self, docs):
#         """
#         Split loaded documents into smaller chunks.
#         Args:
#         - docs (list): List of documents to split.
#         Returns:
#         - list: List of split document chunks.
#         """
#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=Global.config["CHUNK_SIZE"],
#             chunk_overlap=Global.config["CHUNK_OVERLAP"])
#         return text_splitter.split_documents(docs)

#     def generate_embeddings(self, splits):
#         """
#         Generate embeddings for document chunks.
#         Args:
#         - splits (list): List of document chunks.
#         Returns:
#         - list: List of tuples (text, embedding) where embedding is the generated embedding.
#         """
#         texts = [split.page_content for split in splits]
#         embeddings = self.embedding_model.embed_documents(texts)
#         return list(zip(texts, embeddings))

#     def add_embeddings_to_vectorstore(self, embeddings):
#         """
#         Store embeddings in Elasticsearch.
#         Args:
#         - embeddings (list): List of tuples (text, embedding)
#         Returns:
#         - None
#         """
#         for text, embedding in embeddings:
#             self.vectorstore.add_embeddings(
#                 text_embeddings=[(text, embedding)],
#                 refresh_indices=True,
#                 create_index_if_not_exists=True
#             )
#             print(f"Indexed document: {text[:30]}...")

#     def ingest(self):
#         """
#         Execute the entire ingestion process
#         Returns:
#         - None
#         """
#         docs = self.load_documents()
#         splits = self.split_documents(docs)
#         embeddings = self.generate_embeddings(splits)
#         self.add_embeddings_to_vectorstore(embeddings)

# if __name__ == "__main__":
#     file_path = "data/transcript.txt"
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"The file {file_path} does not exist.")

#     ingestor = DocumentIngestor(file_path)
#     ingestor.ingest()



"""
Module: Document Ingestor (Updated for ArXiv Dataset & ChromaDB)
"""
import os
import pandas as pd
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from globals import Global
import json
import shutil
import hashlib


class DocumentIngestor:
    """
    A class to handle ingestion of ArXiv documents into ChromaDB.
    """

        # def ingest(self, limit=None, batch_size=100):
    #   """
    #   Run full ingestion pipeline.
    #   Args:
    #   - limit (int): Limit number of documents.
    #   - batch_size (int): How many documents to ingest at once.
    #   """
    #   docs = self.load_dataset(limit=limit)
    #   split_docs = self.split_documents(docs)

    #   for i in range(0, len(split_docs), batch_size):
    #       batch = split_docs[i:i + batch_size]
    #       self.vectorstore.add_documents(batch)
    #       print(f"Ingested batch {i//batch_size + 1}")
    #   self.vectorstore.persist()
    #   print("Ingestion complete and vectorstore persisted.")

        # def load_dataset(self, limit=None):
    #     """
    #     Load ArXiv dataset from JSON file.
    #     Args:
    #     - limit (int, optional): Max number of rows to load.
    #     Returns:
    #     - List[Document]: LangChain document objects with metadata.
    #     """
    #     df = pd.read_json(self.dataset_path, lines=True)
    #     df = df[['title', 'abstract', 'categories']].dropna(subset=['abstract'])

    #     if limit:
    #         df = df.sample(n=limit, random_state=42)

    #     documents = [
    #         Document(
    #             page_content=row['abstract'],
    #             metadata={
    #                 "title": row['title'],
    #                 "categories": row['categories']
    #             }
    #         )
    #         for _, row in df.iterrows()
    #     ]

    #     return documents

    def __init__(self, dataset_path, config_path='config/config.json'):
        """
        Args:
        - dataset_path (str): Path to the ArXiv dataset JSON file.
        - config_path (str, optional): Path to the config JSON file.
        """
        self.dataset_path = dataset_path
        Global.init(config_path)

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=Global.config["HUGGINGFACE_MODEL"]
        )

        self.vectorstore = Chroma(
            embedding_function=self.embedding_model,
            persist_directory=Global.config.get("CHROMA_PERSIST_DIR", "./chroma_db")
        )

    def load_dataset(self, limit=None):
        """
        Efficiently load documents from a large JSON file (line-by-line).
        """
        documents = []
        with open(self.dataset_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if limit and i >= limit:
                    break
                try:
                    record = json.loads(line)
                    if 'abstract' in record and record['abstract']:
                        documents.append(Document(
                            page_content=record['abstract'],
                            metadata={
                                "title": record.get('title', ''),
                                "categories": record.get('categories', '')
                            }
                        ))
                except json.JSONDecodeError as e:
                    print(f"Error decoding line {i}: {e}")
                    continue
        return documents

    def split_documents(self, documents):
        """
        Split documents into chunks.
        Args:
        - documents (list): List of LangChain Document objects.
        Returns:
        - list: Split documents.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Global.config["CHUNK_SIZE"],
            chunk_overlap=Global.config["CHUNK_OVERLAP"]
        )
        return text_splitter.split_documents(documents)

    def ingest(self, limit=None, batch_size=100):
        """
        Run full ingestion pipeline.
        Args:
        - limit (int): Limit number of documents.
        - batch_size (int): How many documents to ingest at once.
        """
        docs = self.load_dataset(limit=limit)
        split_docs = self.split_documents(docs)
        seen_hashes = set()

        for i in range(0, len(split_docs), batch_size):
            batch = split_docs[i:i + batch_size]
            
            unique_batch = []
            unique_ids = []

            for doc in batch:
                doc_hash = self.hash_doc(doc)
                if doc_hash not in seen_hashes:
                    seen_hashes.add(doc_hash)
                    unique_batch.append(doc)
                    unique_ids.append(doc_hash)

            if unique_batch:
                self.vectorstore.add_documents(unique_batch, ids=unique_ids)
                print(f"Ingested unique batch {i//batch_size + 1}")

    def hash_doc(self, doc):
        content = doc.page_content + doc.metadata.get("title", "")
        return hashlib.md5(content.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    dataset_path = "src/arxiv-metadata-oai-snapshot.json"

    if os.path.exists('./chroma_db'):
        shutil.rmtree('./chroma_db')

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"The dataset {dataset_path} does not exist.")

    ingestor = DocumentIngestor(dataset_path)
    ingestor.ingest(limit=50000)