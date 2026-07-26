from modules.agents.ruby_agent import RubyAgent

agent = RubyAgent()

mission = agent.create_mission(
    "search google robotics"
)

print(mission)