from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


chat_model = ChatOpenAI(openai_api_key=api_key)

template = """You are a helpful assistant that generates comma separated lists.
            A user will pass in a category, and you should generate 5 objects in that category
            Only return a comma separated list and nothing more."""

human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
result = chain.invoke({'text': 'colors'})
print(result)
