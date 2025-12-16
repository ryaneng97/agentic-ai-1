from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

#Load API Key
API_KEY = os.environ["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    api_key=API_KEY
)                   

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="You are a helpful assistant",
)

response = agent.invoke({"messages": [{"role": "user", "content": "What is the weather in Derry, Northern Ireland?"}]})

print(response)