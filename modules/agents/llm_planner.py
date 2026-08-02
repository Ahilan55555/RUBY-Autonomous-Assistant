import json
import time

from modules.llm.ollama_client import (
    ask_llm
)

from core.schemas.task_schema import (
    Task
)

from core.schemas.plan_schema import (
    Plan
)

from core.capability_registry_v2 import (
    capability_summary
)

from modules.agents.context_agent import (
    ContextAgent
)


class LLMPlanner:

    def plan(
        self,
        goal,
        context=None
    ):

        llm_start = time.time()

        # ---------------------------------
        # Build Planning Context
        # ---------------------------------

        if context is None:

            context = (
                ContextAgent()
                .build_context()
            )

        capabilities = capability_summary()

        # ---------------------------------
        # Planner Prompt
        # ---------------------------------

        prompt = f"""
You are Ruby's planning engine.

Your responsibility is ONLY to create executable plans.

=========================
CURRENT GOAL
=========================

{goal}

=========================
CURRENT CONTEXT
=========================

{context}

=========================
AVAILABLE CAPABILITIES
=========================

{capabilities}

=========================
PLANNING RULES
=========================

1. ONLY use the capabilities listed above.

2. NEVER invent new intents.

3. NEVER invent new targets.

4. NEVER invent capabilities.

5. NEVER assume a website unless the user explicitly requests one.

6. If the command is ambiguous, use the current context to choose the safest interpretation.

7. Prefer the smallest valid plan.

8. Think step by step before producing the plan.

9. Return ONLY valid JSON.

=========================
OUTPUT FORMAT
=========================

{{
    "goal": "...",
    "tasks": [
        {{
            "intent": "...",
            "target": "...",
            "query": "..."
        }}
    ]
}}
"""

        print("\n========== PLANNER PROMPT ==========")
        print(prompt)
        print("====================================\n")

        # ---------------------------------
        # Call LLM
        # ---------------------------------

        print("\n========== CAPABILITY SUMMARY ==========")
        print(capabilities)
        print("========================================\n")

        response = ask_llm(
            prompt
        )

        print(
            "[LLM TIME]",
            time.time() - llm_start
        )

        print("\n===== RAW PLAN =====")
        print(response)
        print("====================\n")

        # ---------------------------------
        # Parse JSON
        # ---------------------------------

        data = json.loads(
            response
        )

        if "intent" in data:

            data = {

                "goal": goal,

                "tasks": [
                    data
                ]
            }

        tasks = []

        for item in data.get(
            "tasks",
            []
        ):

            tasks.append(

                Task(

                    intent=item.get(
                        "intent",
                        ""
                    ),

                    target=item.get(
                        "target",
                        ""
                    ),

                    query=item.get(
                        "query",
                        ""
                    )

                )

            )

        return Plan(

            goal=data.get(
                "goal",
                goal
            ),

            tasks=tasks

        )