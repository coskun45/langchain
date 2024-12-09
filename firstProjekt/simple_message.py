from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    
)

messages = [
    SystemMessage(content="Translate the following from English to Turkish"),
    HumanMessage(content="Hi!")
]

if __name__ == "__main__":
    response = llm.invoke(messages)
    print(response.content)
