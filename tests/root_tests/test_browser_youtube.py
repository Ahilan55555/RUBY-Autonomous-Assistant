from modules.agents.browser_agent import BrowserAgent

agent = BrowserAgent()

print(
    agent.search_youtube(
        "robotics"
    )
)