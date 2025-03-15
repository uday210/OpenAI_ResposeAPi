
from agents import Agent, Runner
import asyncio

Developer_Agent = Agent(
    name="Developer Agent",
    instructions="You are Developer, where you implement the solution on salesforce platform.",
)

Architect_Agent = Agent(
    name="Architect Agent",
    instructions="You are Architect, where you design the solution and ask team to implement the solution on salesforce platform.",
    handoffs=[ Developer_Agent],
)

BA_Agent = Agent(
    name="BA Agent",
    instructions="You are Business Analyst, where you gather requirements and document them. and ask team to implement the solution on salesforce platform.",
    handoffs=[Architect_Agent],
)

async def main():
    result = await Runner.run(BA_Agent, input="I want to stop updating the Accounts if the user profile is CSR.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main()) 

