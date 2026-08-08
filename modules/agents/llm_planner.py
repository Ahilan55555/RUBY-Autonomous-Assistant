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

from core.capability_registry import (
    show_capabilities as show_capabilities_v1
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
                .planner_context()
            )

        runtime_capabilities = capability_summary()

        legacy_capabilities = show_capabilities_v1()

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
LEGACY CAPABILITIES
========================================

{legacy_capabilities}

========================================
PLANNING RULES
========================================

1. ONLY use capabilities listed above.

2. NEVER invent intents.

3. NEVER invent targets.

4. NEVER invent capabilities.

5. NEVER invent UI elements.

6. NEVER assume an application.

7. NEVER assume a browser.

8. NEVER assume a website.

9. If the user says "search",
   do NOT automatically choose Google,
   YouTube or ChatGPT.

10. If multiple interpretations are possible,
    prefer asking for clarification.

11. Never generate tasks Ruby cannot execute.

12. Every task must correspond to an available capability.

13. Do not create placeholder tasks.

14. Prefer the smallest correct plan.

15. Think step-by-step before planning.

16. If the request is impossible,
    return a clarification instead of inventing actions.

17. If a capability is unavailable,
    do not replace it with another capability.

18. Return ONLY valid JSON.

19. Browser capabilities already perform all required browser navigation.

20. NEVER generate an "open_website" task for a browser search.

21. If the user asks to open YouTube and search something, output ONLY:
    intent = browser
    target = search_youtube
    query = the search text

22. If the user asks to open Google and search something, output ONLY:
    intent = browser
    target = search_google
    query = the search text

23. If the user asks to open ChatGPT and send a message, output ONLY:
    intent = browser
    target = ask_chatgpt
    query = the message

24. Browser search capabilities perform navigation themselves.
    Therefore a browser search NEVER needs an additional
    open_website task.

25. For every browser search request, generate EXACTLY ONE task.

26. NEVER generate both:
    open_website + browser

27. NEVER generate open_website when target is:
    search_google
    search_youtube
    ask_chatgpt

IMPORTANT:

For browser requests, the words "open", "go to", or "navigate to"
do NOT mean that an open_website task should be created.

The browser capability itself handles opening and navigating to the website.

Therefore:

"open youtube and search hifi"

MUST become exactly:

{{
    "intent": "browser",
    "target": "search_youtube",
    "query": "hifi"
}}

There must be NO "open_website" task.

"open google and search python"

MUST become exactly:

{{
    "intent": "browser",
    "target": "search_google",
    "query": "python"
}}

There must be NO "open_website" task.

"open chatgpt and say hello"

MUST become exactly:

{{
    "intent": "browser",
    "target": "ask_chatgpt",
    "query": "hello"
}}

There must be NO "open_website" task.

Only Use

intent = browser

with one of these targets:

- search_google
- search_youtube
- ask_chatgpt

Examples:
User:
search music on youtube

Output:

{{
"goal":"search music on youtube",
"tasks":[
{{
"intent":"browser",
"target":"search_youtube",
"query":"music"
}}
]
}}

User:
ask chatgpt hello

Output:

{{
"goal":"ask chatgpt hello",
"tasks":[
{{
"intent":"browser",
"target":"ask_chatgpt",
"query":"hello"
}}
]
}}

========================================
OUTPUT FORMAT
========================================

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

Every browser search MUST include the search text inside "query".


Example:

{{
"intent":"browser",
"target":"search_google",
"query":"python"
}}

Never leave query empty for browser search capabilities.

If clarification is required, return

{{
"status": "clarification",
"question": "...",
"options": [
"...",
"..."
]
}}

User:
just open youtube and search hifi

Output:

{{
"goal":"just open youtube and search hifi",
"tasks":[
{{
"intent":"browser",
"target":"search_youtube",
"query":"hifi"
}}
]
}}

User:
open google and search python

Output:

{{
"goal":"open google and search python",
"tasks":[
{{
"intent":"browser",
"target":"search_google",
"query":"python"
}}
]
}}

User:
open chatgpt and say hello

Output:

{{
"goal":"open chatgpt and say hello",
"tasks":[
{{
"intent":"browser",
"target":"ask_chatgpt",
"query":"hello"
}}
]
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

        print("\n========== LEGACY CAPABILITIES ==========")
        print(legacy_capabilities)
        print("=========================================\n")

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