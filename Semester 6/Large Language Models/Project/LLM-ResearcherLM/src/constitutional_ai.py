from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def refine_answer(initial_question, initial_answer, llm, n = 1):
    principles = [
    "Principle 1: Avoid demeaning, disrespectful, or hateful language toward any individual or group.",
    "Principle 2: Refrain from encouraging violence, harassment, or self-harm.",
    "Principle 3: Ensure responses are respectful."
    ]

    critique_prompt = ChatPromptTemplate.from_messages([
        ("system", f"""
    You are a constitutional assistant trained to critique and revise answers according to the following principles: {principles}.

    Instructions:
    - Do not include labels like "Revised Answer:" or "Note:".
    - Respond with only the final, improved answer.
    - Do not include critiques or explanations.

    Your output should consist of the revised response only.
    """),
        ("human", "Original Question: {question}\nOriginal Answer: {answer}")
    ])


    critique_chain = critique_prompt | llm | StrOutputParser()

    response = initial_answer
    for _ in range(n):
        response = critique_chain.invoke({"question": initial_question, "answer": response})

    return response
