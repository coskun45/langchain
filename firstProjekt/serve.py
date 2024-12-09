from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import Json
from fastapi import FastAPI
from langserve import add_routes

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
app =FastAPI()
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    print(chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
))