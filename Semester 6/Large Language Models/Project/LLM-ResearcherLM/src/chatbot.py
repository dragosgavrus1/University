# """
# Module: Chatbot
# """
# import matplotlib.pyplot as plt
# from sklearn.manifold import TSNE
# import numpy as np
# from langchain_elasticsearch import ElasticsearchStore
# from langchain_openai import AzureChatOpenAI
# from langchain.schema import AIMessage, HumanMessage
# from elasticsearch import Elasticsearch
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.output_parsers import StrOutputParser
# import gradio as gr
# from globals import Global


# class ChatBot:
#     """
#     A chatbot class for handling document ingestion, processing, and chat interactions.
#     """

#     def __init__(self):
#         """Initialize chatbot with config."""
#         self._log = Global.get_logger(__name__)
#         self._log.info('Chatbot instance created')
#         self.initialize_components()

#     def initialize_components(self):
#         """Initialize components."""
#         self.llm = AzureChatOpenAI(     # Change to LLM Studio llm
#             azure_deployment=Global.config["AZURE_DEPLOYMENT"],
#             azure_endpoint=Global.config["AZURE_ENDPOINT"],
#             api_key=Global.config["OPENAI_API_KEY"],
#             api_version="2024-05-01-preview"
#         )

#         self.all_embeddings = []
#         self.labels = []

#         self.embedding_model = HuggingFaceEmbeddings(
#             model_name=Global.config["HUGGINGFACE_MODEL"])

#         self.es_connection = Elasticsearch(Global.config["ELASTICSEARCH_URL"])  # Change to VectorStore

#         self.vectorstore = ElasticsearchStore(  # Change to VectorStore
#             embedding=self.embedding_model,
#             index_name=Global.config["INDEX_NAME"],
#             es_connection=self.es_connection
#         )

#         self.retriever = self.vectorstore.as_retriever(
#             search_type="similarity", search_kwargs={"k": 6})

#         self.combined_system_prompt = Global.config["SYSTEM_PROMPT"]

#         self.combined_prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", self.combined_system_prompt),
#                 MessagesPlaceholder("chat_history", optional=True),
#                 ("human", "{question}"),
#             ]
#         )

#         self.combined_chain = self.combined_prompt | self.llm | StrOutputParser()

#     def format_docs(self, docs):
#         """Format documents."""
#         return "\n\n".join(doc.page_content for doc in docs)

#     def format_chat_history(self, history):
#         """Format chat history."""
#         history_langchain_format = []
#         start_index = max(0, len(history) - 15)
#         recent_history = history[start_index:]

#         for human, ai in recent_history:
#             history_langchain_format.append(HumanMessage(content=human))
#             history_langchain_format.append(AIMessage(content=ai))

#         return history_langchain_format

#     def get_context(self, question):
#         """Retrieve context."""
#         return self.retriever.invoke(question)

#     def process_chat(self, new_question, chat_history):
#         """Process chat."""
#         formatted_chat_history = self.format_chat_history(chat_history)
#         context = self.get_context(new_question)
#         formatted_context = self.format_docs(context)

#         combined_output = self.combined_chain.invoke({
#             'chat_history': formatted_chat_history,
#             'question': new_question,
#             'context': formatted_context
#         })

#         self._log = Global.get_logger(__name__)
#         self._log.info('Response generated')

#         return combined_output

#     def launch_bot(self):
#         """Launch chatbot."""
#         answer_bot = gr.ChatInterface(
#             self.process_chat,
#             chatbot=gr.Chatbot(
#                 height=300),
#             textbox=gr.Textbox(
#                 placeholder="Ask me a question",
#                 container=False,
#                 scale=7),
#             title="ChatBot",
#             theme="soft",
#             submit_btn="Ask")
#         answer_bot.launch()


# ================================================================================================================================================

#ne trb baza de date
# populate chroma db (vectorstroe) for ragging
# folosit variabila "retriever"
# trb pus in prompt si contexrt scos din db cu retriever

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
from langchain_elasticsearch import ElasticsearchStore
from langchain_openai import AzureChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, Document
from elasticsearch import Elasticsearch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import gradio as gr
from langchain_community.vectorstores import Chroma
from ingestion.globals import Global
from constitutional_ai import refine_answer


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
        self.llm = ChatOpenAI(
            base_url="http://localhost:1234/v1",  # LM Studio default local URL
            api_key="lm-studio",  # Dummy key, LM Studio usually doesn't validate it
            #model="llama-3.2-3b-instruct",  # e.g., "gpt-3.5-turbo", "mistral", etc.
            model= "gemma-2-2b-it"
        )

        self.all_embeddings = []
        self.labels = []

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=Global.config["HUGGINGFACE_MODEL"])

        #self.es_connection = Elasticsearch(Global.config["ELASTICSEARCH_URL"])  # Change to VectorStore

        self.vectorstore = Chroma(
            embedding_function=self.embedding_model,
            persist_directory=Global.config.get("CHROMA_PERSIST_DIR", "./chroma_db")  # optional, local folder to persist data
        )

        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity", search_kwargs={"k": 6})

        self.combined_system_prompt = Global.config["SYSTEM_PROMPT"]

        self.combined_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.combined_system_prompt),
                MessagesPlaceholder("chat_history", optional=True),
                MessagesPlaceholder("rules", optional=True),
                ("human", "{question}"),
            ]
        )

        self.rules_prompt = Global.config["CHAT_RULES_PROMPT"]
        self.combined_rules_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.rules_prompt),
                MessagesPlaceholder("chat_history"),
            ]
        )

        self.combined_chain = self.combined_prompt | self.llm | StrOutputParser()
        self.combined_rules_chain = self.combined_rules_prompt | self.llm | StrOutputParser()

    def format_docs(self, docs):
        """Format documents."""
        return "\n\n".join(doc.page_content for doc in docs)
    
    def process_chat(self, new_question, chat_history):
        """Process chat."""
        formatted_chat_history = self.format_chat_history(chat_history)
        context_docs = self.get_context(new_question)
        
        if not context_docs or all(len(doc.page_content.strip()) == 0 for doc in context_docs):
            # If no meaningful context found
            return "I don't know."

        formatted_context = self.format_docs(context_docs)

        combined_output = self.combined_chain.invoke({
            'chat_history': formatted_chat_history,
            'question': new_question,
            'context': formatted_context,
            'rules': self.combined_rules_chain.invoke({
                'chat_history': formatted_chat_history
            })
        })

        self._log = Global.get_logger(__name__)
        self._log.info('Response generated')

        self._log.info(combined_output)

        output = refine_answer(new_question, combined_output, self.llm)

        qa_text = f"Q: {new_question}\nA: {output}"
        new_doc = Document(page_content=qa_text)
        self.vectorstore.add_documents([new_doc])

        return output
    

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

    # def process_chat(self, new_question, chat_history):
    #     """Process chat."""
    #     formatted_chat_history = self.format_chat_history(chat_history)
    #     context = self.get_context(new_question)
    #     formatted_context = self.format_docs(context)

    #     combined_output = self.combined_chain.invoke({
    #         'chat_history': formatted_chat_history,
    #         'question': new_question,
    #         'context': formatted_context
    #     })

    #     self._log = Global.get_logger(__name__)
    #     self._log.info('Response generated')

    #     return combined_output

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
