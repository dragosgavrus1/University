import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from ingestion.globals import Global
from chatbot import ChatBot
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
import re

Global.init('config/config.json')
chat_bot = ChatBot()

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def embed(text):
    """Get vector embedding."""
    return np.array(embedding_model.embed_query(text)).reshape(1, -1)

def similarity(a, b):
    """Compute cosine similarity."""
    return cosine_similarity(embed(a), embed(b))[0][0]

def extract_paper_ids(text):
    """Extract Paper IDs like 0704.0001 from output text."""
    pattern = r"\b\d{4}\.\d{4}\b"
    return re.findall(pattern, text)

def compute_citation_score(output_text, expected_ids):
    """Compute citation precision-recall F1 score."""
    extracted_ids = extract_paper_ids(output_text)
    if not extracted_ids:
        return 0.0
    hits = len(set(extracted_ids) & set(expected_ids))
    precision = hits / len(extracted_ids)
    recall = hits / len(expected_ids)
    f1_score = (2 * precision * recall) / (precision + recall + 1e-8)
    return f1_score

def build_context(docs):
    """
    Build a rich, structured context string from a list of Chroma documents.
    Each document will include metadata like id, title, authors, and abstract.
    """
    context_chunks = []
    
    for doc in docs:
        meta = doc.metadata
        page_content = doc.page_content.strip()

        paper_id = meta.get("id", "Unknown ID")
        title = meta.get("title", "Unknown Title")
        authors = meta.get("authors", "Unknown Authors")
        categories = meta.get("categories", "Unknown Categories")
        abstract = meta.get("abstract", page_content)

        context_block = (
            f"Paper ID: {paper_id}\n"
            f"Title: {title}\n"
            f"Authors: {authors}\n"
            f"Categories: {categories}\n"
            f"Abstract: {abstract.strip()}\n"
            "----"
        )
        context_chunks.append(context_block)
    
    return "\n\n".join(context_chunks)


#test_question = "Can you please help me find research papers regarding biology?"
# prompt_templates = {
#     "Original Prompt": Global.config["SYSTEM_PROMPT"],
#     "More Formal": """Given the chat history and the latest user query, reformulate it into a standalone question. Answer using only the provided technical context. Be concise and formal, use maximum three sentences. If uncertain, state so. Chat History: {chat_history} Question: {question} Context: {context} Reformulated Question and Answer:""",
#     "Friendly Style": """Make the user question independent of chat history. Based on the given documents and context, provide a short, friendly, easy-to-read answer (3 sentences max). If unknown, say you don't know. Chat History: {chat_history} Question: {question} Context: {context} Reformulated Question and Answer:""",
#     "Extract-only": """Using only the information provided in the context, answer the following user question. Do not use any external knowledge. If the answer cannot be fully found in the context, respond with "I don't know." Limit your answer to three concise sentences maximum.  Chat History: {chat_history}  Question: {question}  Context: {context}  Answer:""",
#     "Strict Context-Only": """Answer the user question based strictly on the given context. Do not add external knowledge, interpretations, or assumptions. If the context does not contain the answer, state "I don't know." Keep the answer short, direct, and factual (maximum three sentences).  Chat History: {chat_history}  Question: {question}  Context: {context} Precise Answer:""",
#     "Fact-based Compact": """Formulate a precise, factual answer to the user's question using only the provided context. Use clear and compact sentences. If no sufficient information is available, answer with "I don't know." Do not rephrase or summarize — directly extract. Chat History: {chat_history} Question: {question} Context: {context} Fact-based Answer:""",
#     "Context Fidelity": """You are an assistant answering questions strictly based on provided context information. Avoid incorporating knowledge not found in the context. When unsure or if information is missing, respond with "I don't know." Your answer must be factually faithful to the context and under three sentences. Chat History: {chat_history} Question: {question} Context: {context} Response:""",
#     "Claude Variation 1": """Given the chat history and the user's question, provide an answer based exclusively on the research papers in the context. Do not incorporate external knowledge. Cite specific papers when possible. If the research doesn't address the question, state "The available research does not cover this topic." Maximum 3 sentences. Chat History: {chat_history} Question: {question} Context: {context} Research-Based Answer:""",
#     "Claude Variation 2": """Review the entire conversation history and current question, then answer using only information found in the provided research papers. Maintain scientific precision and avoid speculation beyond the evidence. If information is insufficient, acknowledge the limitations clearly. Keep your response under 3 sentences. Chat History: {chat_history} Question: {question} Context: {context} Evidence-Supported Response:""",
#     "Claude Variation 3": """Taking into account the previous conversation and the current query, extract relevant information solely from the provided research papers to formulate your answer. Do not add external knowledge or assumptions. If the papers don't contain sufficient information, respond with "The research papers don't provide enough information on this topic." Maximum 3 sentences. Chat History: {chat_history} Question: {question} Context: {context} Literature-Based Answer:""",
#     "Claude Variation 4": """Considering both the chat history and the current question, formulate a response using exclusively the information in the provided research context. If multiple papers present conflicting results, note this briefly. If the answer cannot be determined from the provided papers, state "This question cannot be answered from the available research." Limit to 3 sentences. Chat History: {chat_history} Question: {question} Context: {context} Research Summary:""",
#     "Claude Variation 5": """After reviewing the conversation history and the latest query, answer based strictly on the scientific papers provided in the context. Maintain academic rigor and cite specific studies when relevant. If the research is inconclusive or the papers don't address the question, clearly state this limitation. Maximum 3 sentences. Chat History: {chat_history} Question: {question} Context: {context} Academic Response:""",
#     "Gemini prompt 1":"""Identify the primary research question addressed in the provided text. Answer concisely in a single sentence. Chat History: {chat_history} Question: What is the main question? Context: {context} Research Question:""",
#     "Gemini prompt 2":"""Based on the following document, what methodology was employed in the study? Describe it briefly, using a maximum of two sentences. Chat History: {chat_history} Question: How was the research conducted? Context: {context} Methodology:""",
#     "Gemini prompt 3":"""Extract the key findings or results presented in the provided research paper. List them concisely, with a maximum of three bullet points. Chat History: {chat_history} Question: What were the main results? Context: {context} Key Findings:""",
#     "Gemini prompt 4":"""According to the text, what are the limitations of the research discussed? Answer in one sentence, if mentioned. Chat History: {chat_history} Question: What are the study's limitations? Context: {context} Limitations:""",
#     "Gemini prompt 5":"""What are the keywords or index terms associated with this research paper, as mentioned in the text? List up to three. Chat History: {chat_history} Question: What are the keywords? Context: {context} Keywords:""",
#     "Deepseek 1": """Using only the provided research context, answer the user's question directly. If the information is not found, reply 'I don't know.' Keep the response under three sentences. Chat History: {chat_history} Question: {question} Context: {context} Answer:""",
#     "Deepseek 2": """Extract the exact answer to the user's question from the given research context. Do not infer or add details. Respond with 'I don't know' if unclear. Chat History: {chat_history} Question: {question} Context: {context} Exact Answer:""",
#     "Deepseek 3": """Provide a one-sentence answer to the question based strictly on the research context. Omit if unsupported. Chat History: {chat_history} Question: {question} Context: {context} Short Answer:""",
#     "Deepseek 4": """Search the provided research documents for a factual answer to the question. Cite directly or state 'I don't know.' Chat History: {chat_history} Question: {question} Context: {context} Cited Answer:""",
#     "Deepseek 5": """Answer the user's question verbatim from the research context. No paraphrasing. If absent, say so. Chat History: {chat_history} Question: {question} Context: {context} Verbatim Answer:""",
#     "Deepseek 6": """Generate a bullet-point summary from the context to answer the question. Max 2 bullets. If irrelevant, state 'I don't know.' Chat History: {chat_history} Question: {question} Context: {context} Summary:""",
#     "Deepseek 7": """Identify the most relevant sentence from the context to answer the question. Return it directly or 'I don't know.' Chat History: {chat_history} Question: {question} Context: {context} Relevant Sentence:""",
#     "prompt 1": """Use only the given research context to answer the user's question. Do not rely on general knowledge. If the context lacks the information, respond with "I don't know." Answer in 1–2 sentences maximum. Chat History: {chat_history} Question: {question} Context: {context} Answer:""",
#     "prompt 2": """Extract specific information from the provided context to answer the user's question. If no clear information is available, reply "I don't know." Avoid generic statements. Answer briefly and factually. Chat History: {chat_history} Question: {question} Context: {context} Direct Answer:""",
#     "prompt 3": """Identify a sentence from the provided context that directly answers the user's question. Return the sentence exactly or say "I don't know" if none is relevant. Do not summarize or speculate. Chat History: {chat_history} Question: {question} Context: {context} Sentence:""",
#     "prompt 4": """Based solely on the given documents, provide an evidence-supported answer to the user's question. Mention the specific document (e.g., Doc1) if possible. If insufficient evidence exists, state "I don't know." Limit the response to two sentences. Chat History: {chat_history} Question: {question} Context: {context} Evidence-Based Response:""",
#     "prompt 5": """Search only within the context for an exact answer. If no clear match is found, reply "I don't know." Provide a short, precise, technical answer (max 2 sentences). No external knowledge allowed. Chat History: {chat_history} Question: {question} Context: {context} Exact Response:""",
#     "prompt 6": """Using strictly the information available in the context, answer the user's question. If multiple pieces of evidence exist, mention them briefly. If none exist, say "I don't know." Keep the response under three sentences. Chat History: {chat_history} Question: {question} Context: {context} Context-Based Answer:""",
#     "prompt 7": """Directly quote relevant sentences from the context to answer the question. Do not paraphrase. If the context is irrelevant, say "I don't know." Return either a quote or 'I don't know'. Chat History: {chat_history} Question: {question} Context: {context} Quoted Answer:""",
#     "prompt 8": """Review the documents provided. If an answer exists, cite the source document name (e.g., Doc1) and answer in a concise factual style. If no answer is possible, reply "I don't know." No external assumptions allowed. Chat History: {chat_history} Question: {question} Context: {context} Cited Answer:""",
#     "prompt 9": """Answer the user's question using only facts extracted directly from the context. If any information is missing, respond with "I don't know." Write clearly and in under two sentences. Chat History: {chat_history} Question: {question} Context: {context} Fact-Extracted Answer:""",
#     "prompt 10": """When answering the user's question, rely exclusively on the context provided. Mention if evidence is inconclusive. Avoid introducing external content. Maximum three sentences. Chat History: {chat_history} Question: {question} Context: {context} Document-Backed Answer:""",
#     "prompt 11": """Analyze the provided documents carefully. Answer the user’s question using only the evidence contained in them. If no sufficient information is found, respond with "I don't know." Keep your response under three factual sentences. Cite document titles if appropriate. Chat History: {chat_history} Question: {question} Context: {context} Document-Based Response:""",
#     "prompt 12": """You are an expert research assistant. Answer the user’s query strictly using content from the provided context. Do not infer, summarize beyond the source, or hallucinate. If the context does not fully support an answer, say "I don't know." Response should be precise and 2 sentences maximum. Chat History: {chat_history} Question: {question} Context: {context} Expert Answer:""",
#     "prompt 13": """From the documents given, locate any direct answer to the user’s question. If found, state it concisely along with the document source (e.g., 'according to Doc1'). If not, clearly reply "I don't know." Avoid paraphrasing or external speculation. Keep it under three sentences. Chat History: {chat_history} Question: {question} Context: {context} Direct Sourced Answer:""",
#     "prompt 14": """Given the research context, produce a response that is strictly fact-based. Prioritize quoting or referencing the source documents if relevant. If no information matches, answer "I don't know." Avoid generalizations or assumptions. Limit your reply to two clear sentences. Chat History: {chat_history} Question: {question} Context: {context} Factual Response:""",
#     "prompt 15": """Carefully scan the context documents. Answer the user’s query using exact phrasing when possible. If the documents lack sufficient coverage, state "I don't know." Provide a response of no more than two sentences, maintaining research paper-level factuality. Chat History: {chat_history} Question: {question} Context: {context} Verbatim-Based Answer:""",
#     "prompt 16": """You are tasked with providing scientifically faithful answers based only on the given documents. If the information is partial or absent, clearly acknowledge it ("I don't know."). Never assume or complete missing information. Keep your answer under 3 short sentences, and if possible mention the document used. Chat History: {chat_history} Question: {question} Context: {context} Faithful Scientific Response:""",
#     "prompt 17": """Scan the research context. If a direct or near-direct answer exists, return it exactly or minimally reformulated. If no appropriate evidence is found, reply "I don't know." The answer must be evidence-supported and concise (max 2 sentences). Chat History: {chat_history} Question: {question} Context: {context} Minimalist Evidence Answer:""",
#     "Optimized Prompt 1": """You are an academic assistant. Your task is to answer user questions strictly based on the provided papers. Each paper includes a Paper ID, Title, Authors, Categories, and Abstract. Do not invent facts. If no information matches the question, reply "I don't know." If citing, use the Paper ID. Be concise (2-3 sentences).""",
#     "Optimized Prompt 2": """Given a structured list of research papers (with Paper ID, Title, Authors, Categories, Abstract), answer the user question accurately using only this data. If you refer to a paper, include its ID. Avoid speculation. If no matching information exists, reply: "The available research does not cover this topic." Limit answers to 3 sentences maximum.""",
#     "Optimized Prompt 3": """Answer the user's question based exclusively on the provided academic entries. Cite using Paper ID if referring to a document. If the context does not sufficiently cover the topic, explicitly say: "No information found in the provided papers." Be direct, factual, and keep the response under three sentences.""",
#     "Optimized Prompt 4": """You have access to multiple academic research entries. Each entry provides ID, Title, Authors, Categories, and Abstract. Rely only on this information. If evidence is unclear or missing, say "I don't know." Prefer citing specific Paper IDs if giving an answer. Keep the style formal and scientific.""",
#     "Optimized Prompt 5": """Based on the provided research papers (containing ID, Title, Authors, Categories, Abstract), answer the user's question. Your response must be grounded only in the given information. Reference the Paper ID when possible. If no sufficient data is available, politely state it. Do not introduce external knowledge. Answer in no more than three sentences."""
# }
#test_context = """Doc1: Title: "Adaptations of Mammals to Climate Change". Abstract: This study examines physiological and behavioral adaptations of mammalian species in response to changing environmental temperatures and precipitation patterns. Doc2: Title: "Aquatic Plant Genetics in Freshwater Ecosystems". Abstract: This paper investigates the genetic diversity of freshwater plant species and how it influences ecosystem resilience to pollution and climate variations. Doc3: Title: "Cellular Mechanisms of Plant Growth Under Water Stress". Abstract: Research focused on how drought conditions affect cell expansion and gene expression in key crop species such as maize and wheat. Doc4: Title: "Applications of Mathematical Modeling in Water Resource Management". Abstract: While this study involves water systems, it focuses on computational simulations and does not explore biological aspects."""


prompt_templates = {
    "Original Prompt": Global.config["SYSTEM_PROMPT"],
    "Fact-based Compact": """Formulate a precise, factual answer to the user's question using only the provided context. Use clear and compact sentences. If no sufficient information is available, answer with "I don't know." Do not rephrase or summarize — directly extract. Chat History: {chat_history} Question: {question} Context: {context} Fact-based Answer:""",
    "Deepseek 4": """Search the provided research documents for a factual answer to the question. Cite directly or state 'I don't know.' Chat History: {chat_history} Question: {question} Context: {context} Cited Answer:""",
    "prompt 4": """Based solely on the given documents, provide an evidence-supported answer to the user's question. Mention the specific document (e.g., Doc1) if possible. If insufficient evidence exists, state "I don't know." Limit the response to two sentences. Chat History: {chat_history} Question: {question} Context: {context} Evidence-Based Response:""",
    "prompt 6": """Using strictly the information available in the context, answer the user's question. If multiple pieces of evidence exist, mention them briefly. If none exist, say "I don't know." Keep the response under three sentences. Chat History: {chat_history} Question: {question} Context: {context} Context-Based Answer:""",
    "Ultra Prompt 1": """You must answer the user's question using only the provided research context (Paper ID, Title, Abstract, etc.).If an answer exists, cite the Paper ID explicitly. If multiple papers are relevant, mention them briefly. If no relevant information exists, respond precisely: "I don't know." Your response must be concise (maximum 2 sentences), factual, and without any external assumptions. Chat History: {chat_history} Question: {question} Context: {context} Answer:""",
    "Ultra Prompt 2": """Given the structured academic context (Paper ID, Title, Authors, Abstract), find a direct answer to the user's question.Cite the Paper ID if you refer to a paper.If evidence is inconclusive or missing, say exactly: "The context does not provide an answer."Avoid rephrasing abstracts — extract or quote precisely.Limit your answer to under three crisp sentences.Chat History: {chat_history}Question: {question} Context: {context}Response:""",
    "Ultra Prompt 3": """You are a research assistant restricted to the provided papers. Extract exact answers where possible, citing Paper IDs directly.If multiple sources exist, list the most relevant ones by ID.If information is absent, respond "I don't know."Keep the tone academic, concise, and fact-anchored (maximum two sentences).Chat History: {chat_history} Question: {question} Context: {context} Extracted Answer:""",
    "Ultra Prompt 4": """Respond to the user's question based strictly on the given documents (ID, Title, Abstract) State the Paper ID(s) if mentioning studies. If the documents do not answer the question clearly, reply "I don't know." Avoid paraphrasing unless necessary for clarity. Your answer should be factually accurate and within three formal sentences. Chat History: {chat_history} Question: {question} Context: {context} Precise Answer:""",
    "Ultra Prompt 5": """Using only the provided research documents, deliver a scientific, factual answer to the user’s question. Mention the Paper ID for traceability. If evidence is insufficient, say directly: "No information available in the context." Avoid creative rewriting; prioritize direct extraction or minimal rewording. Respond in a precise, academic style in 1–2 sentences. Chat History: {chat_history} Question: {question} Context: {context} Research-Based Answer:""",
    "Faithful Prompt 1": """Strictly answer the user's question by quoting or exactly summarizing sentences from the provided research papers.
Use Paper ID if referring to a document.
Do not add new information or rephrase creatively.
If no matching content is found, respond "I don't know."
Limit your answer to two sentences maximum.
Chat History: {chat_history}
Question: {question}
Context: {context}
Faithful Answer:""",
"Faithful Prompt 2": """You must answer using only phrases or sentences found directly in the provided context (Paper ID, Title, Abstract).
Do not infer, guess, or summarize loosely.
If multiple papers match, list their IDs briefly.
If the question cannot be answered from the text, say "I don't know."
Respond in under three sentences, preserving original meaning exactly.
Chat History: {chat_history}
Question: {question}
Context: {context}
Direct Extract Answer:""",
"Faithful Prompt 3": """Using only exact expressions or close paraphrases from the context, answer the user's question.
If answering, mention the Paper ID cited.
If no sufficient information is available, state clearly: "The context does not answer this question."
Avoid expanding or inferring beyond the documents.
Answer concisely in one or two factual sentences.
Chat History: {chat_history}
Question: {question}
Context: {context}
Context-Bound Answer:""",
"Faithful Prompt 4": """Restrict your answer to exact content provided in the context (Paper ID, Title, Abstract).
Prefer direct quotations or minimal rewording.
If nothing answers the question, respond: "I don't know."
Mention Paper IDs for traceability.
Stay within two factual sentences.
Chat History: {chat_history}
Question: {question}
Context: {context}
Quoted-Based Answer:""",
"Faithful Prompt 5": """Answer the user's query by extracting or lightly paraphrasing sentences from the provided documents.
Only cite Paper IDs if relevant.
If there is no direct match, say: "I don't know."
Keep the tone academic, literal, and faithful to the context.
Answer briefly (max 2 sentences).
Chat History: {chat_history}
Question: {question}
Context: {context}
Literal Context Answer:"""
}


test_question = "Can you find studies about diphoton production at the LHC?"
test_context = """Paper ID: 0704.0001
Title: Calculation of prompt diphoton production cross sections at Tevatron and LHC energies
Abstract: A fully differential calculation in perturbative quantum chromodynamics is presented for the production of massive photon pairs at hadron colliders...

Paper ID: 0704.0002
Title: Sparsity-certifying Graph Decompositions
Abstract: We describe a new algorithm for sparse graph decompositions, related to rigidity theory...

Paper ID: 0704.0003
Title: The evolution of the Earth-Moon system based on the dark matter field fluid model
Abstract: The Earth-Moon system evolution is analyzed through the dark matter field fluid model...
"""

expected_paper_ids = ["0704.0001"]  # Based on topic "diphoton production at LHC" 
records = []

for prompt_name, system_prompt in prompt_templates.items():
    combined_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{question}")
    ])
    combined_chain = combined_prompt | chat_bot.llm | StrOutputParser()

    formatted_chat_history = chat_bot.format_chat_history([])

    output = combined_chain.invoke({
        'chat_history': formatted_chat_history,
        'question': test_question,
        'context': test_context
    })

    # Scores
    relevance_score = similarity(test_question, output)
    faithfulness_score = similarity(test_context, output)
    citation_score = compute_citation_score(output, expected_paper_ids)
    overall_score = 0.4 * relevance_score + 0.4 * faithfulness_score + 0.2 * citation_score

    records.append({
        "Prompt Version": prompt_name,
        "Output": output,
        "Relevance": relevance_score,
        "Faithfulness": faithfulness_score,
        "Citation": citation_score,
        "Overall Score": overall_score
    })

# 5. Results
df = pd.DataFrame(records)
print(df.sort_values(by="Overall Score", ascending=False))

df.to_csv("prompt_evaluation_scored.csv", index=False)