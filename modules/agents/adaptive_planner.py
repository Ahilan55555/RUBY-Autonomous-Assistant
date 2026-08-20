from core.schemas.task_schema import Task

from core.schemas.plan_schema import Plan

from modules.agents.llm_planner import (
    LLMPlanner
)

from modules.memory.strategy_memory import (
    get_best_strategies
)

from modules.agents.context_agent import (
    ContextAgent
)

from modules.agents.planner_validator import (
    PlannerValidator
)

import time


class AdaptivePlanner:

    def __init__(self):

        self.llm = LLMPlanner()

    def recover(self, goal):
        overall_start = time.time()
        start = time.time()

        print(
            "\n[Strategy Rankings]"
        )

        strategies = (
            get_best_strategies()
        )

        for strategy in strategies:

            print(strategy)

        from core.experience_memory import (
            get_best_strategy
        )

        strategy = get_best_strategy(
            goal
        )

        if strategy:

            print(
                "[Adaptive Planner] "
                "Using learned strategy."
            )

            tasks = []

            for step in strategy:

                if step == "open firefox":

                    tasks.append(

                        Task(
                            intent="open_app",
                            target="firefox"
                        )
                    )

                elif step == "search troubleshooting":

                    tasks.append(

                        Task(
                            intent="google_search",
                            query="voice assistant troubleshooting"
                        )
                    )

            return Plan(

                goal=goal,

                tasks=tasks
            )

        goal_lower = goal.lower()

        # -------------------------
        # CONTEXT AWARENESS
        # -------------------------

        context = (

            ContextAgent()

            .build_context()
        )

        state = (

            context["situation"]

            .get(
                "state",
                {}
            )
        )

        active_app = state.get(
            "active_app"
        )

        current_website = state.get(
            "current_website"
        )

        # -------------------------
        # INSPECT PROJECT
        # -------------------------

        if "inspect project" in goal_lower:

            return Plan(

                goal=goal,

                tasks=[

                    Task(
                        intent="file",
                        target="list"
                    ),

                    Task(
                        intent="terminal",
                        target="pwd"
                    )
                ]
            )

        # -------------------------
        # SHOW FILES
        # -------------------------

        if "show files" in goal_lower:

            return Plan(

                goal=goal,

                tasks=[

                    Task(
                        intent="file",
                        target="list"
                    )
                ]
            )

        # -------------------------
        # CURRENT DIRECTORY
        # -------------------------

        if "current directory" in goal_lower:

            return Plan(

                goal=goal,

                tasks=[

                    Task(
                        intent="terminal",
                        target="pwd"
                    )
                ]
            )

        # -------------------------
        # VOICE TROUBLESHOOTING
        # -------------------------

        if "voice" in goal_lower:

            tasks = []

            if active_app != "firefox":

                tasks.append(

                    Task(
                        intent="open_app",
                        target="firefox"
                    )
                )

            tasks.append(

                Task(
                    intent="google_search",
                    query="voice assistant troubleshooting"
                )
            )

            return Plan(

                goal=goal,

                tasks=tasks
            )

        
        # -------------------------
        # RUN MEMORY TEST
        # -------------------------

        if "run memory test" in goal_lower:

            return Plan(

                goal=goal,

                tasks=[

                    Task(
                        intent="python",
                        target="run",
                        query="test_memory.py"
                    )
                ]
            )

        # -------------------------
        # ANALYZE PROJECT
        # -------------------------

        if "analyze project" in goal_lower:

            return Plan(

                goal=goal,

                tasks=[

                    Task(
                        intent="project",
                        target="analyze"
                    )
                ]
            )

        # -------------------------
        # SMART BROWSER REUSE
        # -------------------------

        if (
            active_app == "firefox"
            and current_website == "google"
        ):

            print(
                "[Adaptive Planner] "
                "Reusing active browser context."
            )

        # -------------------------
        # FALLBACK
        # -------------------------

        print(
            "[Adaptive Planner] Using LLM fallback."
        )

        start = time.time()

        planner_start = time.time()

        planner_context = {

            "active_app": active_app,

            "current_website": current_website

        }

        plan = self.llm.plan(

            goal,

            planner_context

        )
        validator = PlannerValidator()

        validation = validator.validate(
            plan
        )

        if not validation["valid"]:

            print()

            print(
                "========== PLANNER VALIDATION FAILED =========="
            )

            print(
                "Intent:",
                validation.get(
                    "intent",
                    "unknown"
                )
            )

            print(
                "Target:",
                validation.get(
                    "target",
                    "unknown"
                )
            )

            print(
                "Reason:",
                validation.get(
                    "reason",
                    "Unknown validation failure."
                )
            )

            print(
                "=============================================="
            )

            return Plan(
                goal=goal,
                tasks=[]
            )



        print(
            "LLM PLAN TIME:",
            time.time() - planner_start
        )

        print(
            f"[PLANNER TIME] "
            f"{time.time()-start:.2f}s"
        )

        print("\n===== FINAL PLAN =====")
        print(plan.tasks)
        print("======================\n")

        print(
            f"[PLANNER TIME] "
            f"{time.time() - start:.2f}s"
        )
        print(
            "TOTAL ADAPTIVE:",
            time.time() - overall_start
        )

        return plan