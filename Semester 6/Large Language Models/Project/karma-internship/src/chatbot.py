"""
Module: Chatbot
"""
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
from langchain_elasticsearch import ElasticsearchStore
from langchain_openai import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from elasticsearch import Elasticsearch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import gradio as gr
from globals import Global


class ChatBot:
    """
    A chatbot class for handling document ingestion, processing, and chat interactions.
    """

    def __init__(self):
        """Initialize chatbot with config."""
        self._log = Global.get_logger(__name__)
        self._log.info('Chatbot instance created')
        self.initialize_components()

    def initialize_components(self):
        """Initialize components."""
        self.llm = AzureChatOpenAI(
            azure_deployment=Global.config["AZURE_DEPLOYMENT"],
            azure_endpoint=Global.config["AZURE_ENDPOINT"],
            api_key=Global.config["OPENAI_API_KEY"],
            api_version="2024-05-01-preview"
        )

        self.all_embeddings = []
        self.labels = []

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=Global.config["HUGGINGFACE_MODEL"])

        self.es_connection = Elasticsearch(Global.config["ELASTICSEARCH_URL"])

        self.vectorstore = ElasticsearchStore(
            embedding=self.embedding_model,
            index_name=Global.config["INDEX_NAME"],
            es_connection=self.es_connection
        )

        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity", search_kwargs={"k": 6})

        self.combined_system_prompt = Global.config["SYSTEM_PROMPT"]

        self.combined_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.combined_system_prompt),
                MessagesPlaceholder("chat_history", optional=True),
                ("human", "{question}"),
            ]
        )

        self.combined_chain = self.combined_prompt | self.llm | StrOutputParser()

    def format_docs(self, docs):
        """Format documents."""
        return "\n\n".join(doc.page_content for doc in docs)

    def format_chat_history(self, history):
        """Format chat history."""
        history_langchain_format = []
        start_index = max(0, len(history) - 15)
        recent_history = history[start_index:]

        for human, ai in recent_history:
            history_langchain_format.append(HumanMessage(content=human))
            history_langchain_format.append(AIMessage(content=ai))

        return history_langchain_format

    def get_context(self, question):
        """Retrieve context."""
        return self.retriever.invoke(question)

    def plot_embeddings(self, question_embedding, context_embeddings, k=6):
        """Plot embeddings."""
        self.all_embeddings.extend([question_embedding] + context_embeddings)
        question_number = (len(self.labels) // (k + 1)) + 1
        self.labels.extend([f"Question {question_number}"] + \
                           [f"Context {question_number}-{i + 1}" for i in range(k)])

        all_embeddings_np = np.array(self.all_embeddings)
        reducer = TSNE(
            n_components=2,
            random_state=42,
            perplexity=min(
                5,
                len(all_embeddings_np) -
                1))
        reduced_embeddings = reducer.fit_transform(all_embeddings_np)

        plt.figure(figsize=(10, 8))
        for i, label in enumerate(self.labels):
            plt.scatter(reduced_embeddings[i, 0],
                        reduced_embeddings[i, 1], label=label)
            plt.annotate(
                label, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]))

        plt.title("Embeddings visualization using TSNE")
        plt.savefig("images/tsne_embeddings.png")

    def process_chat(self, new_question, chat_history):
        """Process chat."""
        formatted_chat_history = self.format_chat_history(chat_history)
        context = self.get_context(new_question)
        formatted_context = self.format_docs(context)

        combined_output = self.combined_chain.invoke({
            'chat_history': formatted_chat_history,
            'question': new_question,
            'context': formatted_context
        })

        question_embedding = self.embedding_model.embed_query(new_question)
        context_embeddings = [
            self.embedding_model.embed_query(
                doc.page_content) for doc in context]

        self.plot_embeddings(question_embedding, context_embeddings)

        self._log = Global.get_logger(__name__)
        self._log.info('Response generated')

        return combined_output

    def launch_bot(self):
        """Launch chatbot."""
        answer_bot = gr.ChatInterface(
            self.process_chat,
            chatbot=gr.Chatbot(
                height=300),
            textbox=gr.Textbox(
                placeholder="Ask me a question",
                container=False,
                scale=7),
            title="ChatBot",
            theme="soft",
            submit_btn="Ask")
        answer_bot.launch()
