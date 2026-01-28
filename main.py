
import spade
import asyncio

class SimpleAgent(spade.agent.Agent):
    async def setup(self):
        print(f"Agent {self.jid} is ready!")

async def main():
    agent = SimpleAgent("agent1@localhost", "password")
    await agent.start()
    
    # Keep running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    spade.run(main())