from core.intent_executor import execute_intent

from core.intent_resolver import resolve_intent

from core.intent_validator import validate_intent

from modules.agents.recovery_agent import RecoveryAgent

from core.goal_manager import complete_goal

from core.goal_manager import fail_goal

from core.event_bus import emit

from core.experience_memory import (
    record_success,
    record_failure
)

import asyncio


class ExecutionAgent:


    def __init__(self):


        self.recovery = RecoveryAgent()


    def execute(self, task):

        resolved_task = resolve_intent(task)
        

        print(resolved_task)


        

        if validate_intent(resolved_task):

            result = execute_intent(
                resolved_task
            )

            if (
                isinstance(result, dict)
                and result.get("success", False)
            ):

                complete_goal(task)

                record_success(

                    str(task),

                    [resolved_task]
                )
            else:

                fail_goal(task)

                record_failure(

                    str(task),

                    [resolved_task]
                )


        else:

            print("Invalid intent:", resolved_task)

            recovered_task = self.recovery.recover(

                resolved_task
            )

            if recovered_task:

                print(

                    "[Execution Agent] Recovery successful."
                )
                asyncio.create_task(

                    emit(

                        "recovery",

                        recovered_task
                    )
                )

                recovery_result = execute_intent(
                    recovered_task
                )

                if (
                    isinstance(recovery_result, dict)
                    and recovery_result.get("success", False)
                ):

                    complete_goal(task)

                else:

                    fail_goal(task)

            else:

                print(

                    "[Execution Agent] Recovery failed."
                )
                fail_goal(task)