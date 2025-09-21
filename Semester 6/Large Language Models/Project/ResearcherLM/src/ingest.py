"""
Module: Document Ingestor
"""
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_elasticsearch import ElasticsearchStore
from langchain_huggingface import HuggingFaceEmbeddings
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
from globals import Global


class DocumentIngestor:
    """
    Class: DocumentIngestor

    A class to handle ingestion of documents from a text file.

    Attributes:
    - file_path
    - embedding_model
    - vectorstore

    Methods:
    - __init__(self, file_path, config_path='config/config.json')
    - load_documents(self)
    - split_documents(self, docs)
    - generate_embeddings(self, splits)
    - add_embeddings_to_vectorstore(self, embeddings)
    - plot_embeddings(self, embeddings)
    - ingest(self)
    """

    def __init__(self, file_path, config_path='config/config.json'):
        """
        Args:
        - file_path (str)
        - config_path (str, optional)
        """
        self.file_path = file_path
        Global.init(config_path)
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=Global.config["HUGGINGFACE_MODEL"])
        self.vectorstore = ElasticsearchStore(      # Change to VectorStore
            embedding=self.embedding_model,
            index_name=Global.config["INDEX_NAME"],
            es_url=Global.config["ELASTICSEARCH_URL"]
        )

    def load_documents(self):
        """
        Load documents from the specified file path.
        Returns:
        - list: List of loaded documents.
        """
        loader = TextLoader(self.file_path)
        return loader.load()

    def split_documents(self, docs):
        """
        Split loaded documents into smaller chunks.
        Args:
        - docs (list): List of documents to split.
        Returns:
        - list: List of split document chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Global.config["CHUNK_SIZE"],
            chunk_overlap=Global.config["CHUNK_OVERLAP"])
        return text_splitter.split_documents(docs)

    def generate_embeddings(self, splits):
        """
        Generate embeddings for document chunks.
        Args:
        - splits (list): List of document chunks.
        Returns:
        - list: List of tuples (text, embedding) where embedding is the generated embedding.
        """
        texts = [split.page_content for split in splits]
        embeddings = self.embedding_model.embed_documents(texts)
        return list(zip(texts, embeddings))

    def add_embeddings_to_vectorstore(self, embeddings):
        """
        Store embeddings in Elasticsearch.
        Args:
        - embeddings (list): List of tuples (text, embedding)
        Returns:
        - None
        """
        for text, embedding in embeddings:
            self.vectorstore.add_embeddings(
                text_embeddings=[(text, embedding)],
                refresh_indices=True,
                create_index_if_not_exists=True
            )
            print(f"Indexed document: {text[:30]}...")

    def ingest(self):
        """
        Execute the entire ingestion process
        Returns:
        - None
        """
        docs = self.load_documents()
        splits = self.split_documents(docs)
        embeddings = self.generate_embeddings(splits)
        self.add_embeddings_to_vectorstore(embeddings)

if __name__ == "__main__":
    file_path = "data/transcript.txt"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    ingestor = DocumentIngestor(file_path)
    ingestor.ingest()
