from modules.agents.browser_agent import BrowserAgent

agent = BrowserAgent()

print(
    agent.ask_chatgpt(
        "What is robotics?"
    )
)