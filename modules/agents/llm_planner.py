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
    planner_capabilities,
    has_capability
)

from modules.agents.context_agent import (
    ContextAgent
)


class LLMPlanner:
    def _parse_json(
        self,
        response
    ):

        response = response.strip()

        if response.startswith("```"):

            lines = response.splitlines()

            if lines:

                lines = lines[1:]

            if lines and lines[-1].strip() == "```":

                lines = lines[:-1]

            response = "\n".join(
                lines
            ).strip()

        return json.loads(
            response
        )

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
                .planner_context()
            )

        runtime_capabilities = planner_capabilities()

        # ---------------------------------
        # Planner Prompt
        # ---------------------------------

        prompt = f"""
You are Ruby's planning engine.

Your only responsibility is to convert a user's goal into a valid executable plan.

========================================
CURRENT GOAL
========================================

{goal}

========================================
CURRENT CONTEXT
========================================

{context}

========================================
RUNTIME V2 CAPABILITIES
========================================

{runtime_capabilities}

========================================
PLANNING RULES
========================================

1. You are selecting from Ruby's available runtime capabilities.

2. ONLY use an exact intent and target combination present
   in RUNTIME CAPABILITIES.

3. NEVER invent an intent.

4. NEVER invent a target.

5. NEVER invent a capability.

6. Choose the capability whose purpose and examples best
   match the user's request.

7. Prefer an existing capability over manually constructing
   low-level actions.

8. Prefer the smallest plan that completely satisfies the goal.

9. A task may use multiple capabilities when the user's goal
   genuinely requires multiple steps.

10. Do not add unnecessary steps.

11. Do not assume an application unless the user's request
    or current context establishes it.

12. Do not assume a website unless the user specifies it
    or the capability itself requires one.

13. Preserve explicit user constraints.

14. If the user explicitly names a destination, application,
    website, or tool, respect that choice.

15. If the request is ambiguous and different capabilities
    would produce meaningfully different results, ask for
    clarification.

16. If no available capability can perform the request,
    return a clarification explaining that the capability
    is unavailable.

17. Every generated task MUST correspond to an available
    runtime capability.

18. Do not create placeholder tasks.

19. Do not generate capabilities that are not listed.

20. Return ONLY valid JSON.

========================================
CAPABILITY SELECTION GUIDANCE
========================================

Use the capability purpose and examples as the primary
source for deciding which capability to select.

Examples:

"scroll down"
→ screen / scroll

"scroll up the page"
→ screen / scroll

"click the text box"
→ screen / click_text

"double click the file"
→ screen / double_click_text

"right click the folder"
→ screen / right_click_text

"open wikipedia.org"
→ browser / open_url

"search python on google"
→ browser / search_google

"search robotics on youtube"
→ browser / search_youtube

"ask ChatGPT what is PID"
→ browser / ask_chatgpt

"run pwd in the terminal"
→ terminal / [available target]

"close Firefox"
→ window / close

"maximize Firefox"
→ window / maximize

The examples above illustrate capability selection.
They do NOT authorize capabilities that are absent
from RUNTIME CAPABILITIES.

========================================
TASK PARAMETERS
========================================

The "query" field contains the user-provided information
required by the selected capability.

Do not unnecessarily modify the user's query.

========================================
SCREEN CAPABILITY PARAMETERS
========================================

For screen/click_text:

The query MUST contain the exact visible text
that Ruby should locate using OCR.

If the user explicitly names visible text,
extract that text into query.

Example:

User:
click Search

Correct:

{{
    "intent": "screen",
    "target": "click_text",
    "query": "Search"
}}

User:
click the "Submit" button

Correct:

{{
    "intent": "screen",
    "target": "click_text",
    "query": "Submit"
}}

Do NOT leave query empty.

If the user describes a UI element semantically
rather than naming visible text, such as:

"click the text box"
"click the search field"
"click the login button"

do NOT invent the text displayed by that element.

Return a clarification instead if no exact visible
text is provided.

For screen/double_click_text:

query MUST contain the visible text to locate.

For screen/right_click_text:

query MUST contain the visible text to locate.

For screen/type_at_text:

query MUST contain both:
1. the visible text identifying the target
2. the text to type

Use this format:

"visible target | text to type"

Example:

User:
type robotics into Search

Correct:

{{
    "intent": "screen",
    "target": "type_at_text",
    "query": "Search | robotics"
}}

For example:

User:
search robotics on youtube

Correct:

{{
    "intent": "browser",
    "target": "search_youtube",
    "query": "robotics"
}}

User:
open wikipedia.org

Correct:

{{
    "intent": "browser",
    "target": "open_url",
    "query": "wikipedia.org"
}}

User:
scroll down

Correct:

{{
    "intent": "screen",
    "target": "scroll",
    "query": "down"
}}
"""

        # ---------------------------------
        # Debug Output
        # ---------------------------------

        print("\n========== CURRENT CONTEXT ==========")
        print(context)
        print("=====================================\n")

        print("\n========== RUNTIME V2 CAPABILITIES ==========")
        print(runtime_capabilities)
        print("=============================================\n")

            
        print("\n========== PLANNER PROMPT ==========")
        print(prompt)
        print("====================================\n")

        # ---------------------------------
        # Call LLM
        # ---------------------------------

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

        try:

            data = self._parse_json(
                response
            )

        except json.JSONDecodeError as error:

            print(
                "[Planner] Invalid JSON:",
                error
            )

            return None

        # ---------------------------------
        # Clarification
        # ---------------------------------

        if data.get("status") == "clarification":

            return data

        # ---------------------------------
        # Normalize Single Task
        # ---------------------------------

        if "intent" in data:

            data = {

                "goal": goal,

                "tasks": [
                    data
                ]

            }

        # ---------------------------------
        # Validate and Build Tasks
        # ---------------------------------

        tasks = []

        for item in data.get(
            "tasks",
            []
        ):

            intent = item.get(
                "intent",
                ""
            )

            target = item.get(
                "target",
                ""
            )

            query = item.get(
                "query",
                ""
            )

            # ---------------------------------
            # Validate Task
            # ---------------------------------

            if not intent or not target:

                print(
                    "[Planner] Invalid task:",
                    item
                )

                return None


            # ---------------------------------
            # Validate Required Query
            # ---------------------------------

            query_required = {
                "screen": {
                    "scroll",
                    "click_text",
                    "double_click_text",
                    "right_click_text",
                    "type_at_text"
                },

                "browser": {
                    "open_url",
                    "search_google",
                    "search_youtube",
                    "ask_chatgpt"
                }
            }


            if (
                intent in query_required
                and target in query_required[intent]
                and not query.strip()
            ):

                print(
                    "[Planner] Missing query:",
                    item
                )

                return None

            # ---------------------------------
            # Validate Capability
            # ---------------------------------

            if not has_capability(
                intent,
                target
            ):

                print(
                    "[Planner] Unknown capability:",
                    intent,
                    target
                )

                return None

            tasks.append(

                Task(

                    intent=intent,

                    target=target,

                    query=query

                )

            )

        # ---------------------------------
        # Reject Empty Plans
        # ---------------------------------

        if not tasks:

            print(
                "[Planner] Empty plan."
            )

            return Plan(
                goal=data.get(
                    "goal",
                    goal
                ),
                tasks=[]
            )
        # ---------------------------------
        # Build Plan
        # ---------------------------------

        return Plan(

            goal=data.get(
                "goal",
                goal
            ),

            tasks=tasks

        )