from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from src.components.prompt import get_anime_prompt
from dotenv import load_dotenv

load_dotenv()


class AnimeRecommender:
    def __init__(self, retriever, model_name: str, temperature: float):
        self.model = ChatGroq(model=model_name, temperature=temperature)
        self.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | get_anime_prompt()
            | self.model
            | StrOutputParser()
        )

    def recommend(self, question: str) -> str:
        response = self.chain.invoke(question)
        return response
