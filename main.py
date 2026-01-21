import asyncio
from mcp_use import MCPClient, MCPAgent
import os
from langchain_groq import ChatGroq

from dotenv import load_dotenv

async def run_memory_chat():
    """Run a chat using MCPAgent's built in conversation memory."""
    load_dotenv()
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API")

    config_file=os.path.abspath("mcp_config.json")

    print("intializing chat.......")


    client=MCPClient.from_config_file(config_file)
    llm=ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")

    agent = MCPAgent(
    llm=llm,
    client=client,
    max_steps=15,
    memory_enabled=True,
    system_prompt=(
        "When calling tools, always use correct JSON types. "
        "Use numbers for numeric fields, not strings."
        "When you use a tool, always read the tool output and "
        "respond with a clear, human-readable answer. "
        "Never return only the tool call."
    )
)


    print("\n======= interactive mcp chat========")
    print("Type exit or quit to end the conversation")
    print("Type clear to clear conversation history")


    try:
        while True:
            user_input=input("\nYou:")

            if user_input.lower() in  ["exit","quit"]:
                print("Ending coversation.....")
                break

            if user_input.lower() =="clear":
                agent.clear_conversation_history()
                print("Conversation history cleared. ")
                continue
            print("\nAssistant: ",end=" ", flush=True)

            try:
                response=await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"\nError: {e}")

    finally:
            if client and client.sessions:
                await client.close_all_sessions()



if __name__=="__main__":
    asyncio.run(run_memory_chat())
