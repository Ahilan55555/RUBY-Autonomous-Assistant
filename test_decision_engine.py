from modules.agents.decision_engine import (
    DecisionEngine
)

from core.task import (
    Task
)

engine = DecisionEngine()

task = Task(
    name="Search"
)

print(

    engine.decide(

        task,

        {

            "completed": True

        }

    )

)

print(

    engine.decide(

        task,

        {

            "completed": False

        }

    )

)