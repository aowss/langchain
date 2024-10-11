from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()

LANGCHAIN_TRACING_V2=os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_API_KEY=os.getenv('LANGCHAIN_API_KEY')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI()
llm.invoke("Hello, world!")