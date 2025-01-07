from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

load_dotenv()

model = ChatOpenAI(model="gpt-4")

search = TavilySearchResults(max_results=2)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]
# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(model, tools)
# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


if __name__ == '__main__':
    response = agent_executor.invoke(
        {"input" : "What is the weather in istanbul now?"}
    )
    print(response)