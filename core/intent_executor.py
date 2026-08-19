from modules.automation.apps import (

    open_firefox,

    open_sublime
)

from modules.memory.strategy_memory import (
    record_strategy
)

from modules.memory.execution_history import (
    record_execution
)

from modules.automation.browser import (

    open_github,

    open_youtube
)



from modules.actions.file_actions import (
    create_file
)
from core.world_state import (
    update_state
)

import time

from core.telemetry import (
    record_execution_time
)

from modules.automation.terminal import (
    run_terminal_command
)

from modules.automation.files import (
    create_folder,
    list_files,
    delete_folder,
    read_file,
    write_file,
    create_file
)

from modules.automation.python_runner import (
    run_python_file
)

from modules.agents.project_understanding_agent import (
    ProjectUnderstandingAgent
)

from modules.agents.research_agent import (
    ResearchAgent
)
from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

from modules.automation.keyboard_controller import (
    type_text,
    press_key,
    hotkey
)

from modules.automation.screen_actions import (
    click_text,
    type_at_text,
    double_click_text,
    right_click_text
)
from modules.automation.window_controller import (
    focus_window,
    close_window,
    minimize_window,
    maximize_window,
    list_windows,
    get_active_window
)

from modules.agents.browser_agent import (
    BrowserAgent
)

from core.capability_registry_v2 import (
    has_capability,
    get_capability,
    planner_capabilities
)

from core.pipeline_executor import PipelineExecutor

from core.mission import Mission

import traceback

from dataclasses import is_dataclass, asdict

browser = BrowserAgent()
pipeline = PipelineExecutor()

def execute_intent(task):

    start_time = time.time()

    if isinstance(task, dict):

        intent = task.get(
            "intent"
        )

        target = task.get(
            "target"
        )

        query = task.get(
            "query"
        )

    else:

        intent = task.intent

        target = task.target

        query = task.query


    # ---------------------------------
    # CAPABILITY CHECK
    # ---------------------------------
    print(
        "CAPABILITY CHECK:",
        intent,
        target
    )

    

    print(
        "HAS:",
        has_capability(
            intent,
            target
        )
    )
    if not has_capability(

        intent,

        target
    ):

        error_message = (

            f"Capability not supported: "
            f"{intent} -> {target}"
        )

        print(error_message)
        print(
            f"Capability not supported:"
            f" {task}"
        )

        result = {

            "success": False,

            "error": error_message
        }

        record_execution(
            task,
            result
        )

        record_strategy(
            intent,
            False
        )

        return result


    try:

        # ---------------------------------
        # OPEN APPLICATIONS
        # ---------------------------------

        if intent == "open_app":

            if target == "firefox":

                open_firefox()

                update_state(
                    "active_app",
                    "firefox"
                )

            elif target == "sublime":

                open_sublime()

                update_state(
                    "active_app",
                    "sublime"
                )

            else:

                result = {

                    "success": False,

                    "error": "Unknown app target"
                }

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result


        # ---------------------------------
        # OPEN WEBSITES
        # ---------------------------------

        elif intent == "open_website":

            if target == "github":

                open_github()

                update_state(
                    "current_website",
                    "github"
                )

            elif target == "youtube":

                open_youtube()

                update_state(
                    "current_website",
                    "youtube"
                )

            else:

                result = {

                    "success": False,

                    "error": "Unknown website target"
                }

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result


        # ---------------------------------
        # PYTHON EXECUTION
        # ---------------------------------

        elif intent == "python":

            result = run_python_file(
                query
            )

            print(result)

            update_state(
                "last_python_file",
                query
            )

            if not result["success"]:

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result


        # ---------------------------------
        # TERMINAL COMMANDS
        # ---------------------------------

        elif intent == "terminal":

            result = run_terminal_command(
                target
            )

            print(result)

            update_state(
                "last_terminal_command",
                target
            )

            if not result["success"]:

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result


        # ---------------------------------
        # FILE OPERATIONS
        # ---------------------------------

        elif intent == "file":

            result = None

            if target == "list":

                result = list_files()

            elif target == "create_folder":

                result = create_folder(
                    query
                )
            elif target == "create_file":

                result = create_file(
                    query
                )

            elif target == "delete_folder":

                result = delete_folder(
                    query
                )

            elif target == "read":

                result = read_file(
                    query
                )

            elif target == "write":

                parts = query.split(
                    "|",
                    1
                )

                if len(parts) != 2:

                    result = {

                        "success": False,

                        "error": "Invalid write format"
                    }

                    record_execution(
                        task,
                        result
                    )

                    record_strategy(
                        intent,
                        False
                    )

                    return result

                file_path = parts[0]

                content = parts[1]

                result = write_file(
                    file_path,
                    content
                )

            else:

                result = {

                    "success": False,

                    "error": "Unknown file target"
                }

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result

            print(result)

            update_state(
                "last_file_operation",
                target
            )

            if not result["success"]:

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result


        # ---------------------------------
        # PROJECT ANALYSIS
        # ---------------------------------

        elif intent == "project":

            if target == "analyze":

                result = (

                    ProjectUnderstandingAgent()

                    .analyze()
                )

                print(result)

                update_state(
                    "last_project_action",
                    "analyze"
                )

                if not result["success"]:

                    record_execution(
                        task,
                        result
                    )

                    record_strategy(
                        intent,
                        False
                    )

                    return result

            else:

                result = {

                    "success": False,

                    "error": "Unknown project target"
                }

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result


        # ---------------------------------
        # GOOGLE SEARCH
        # ---------------------------------

        elif intent == "google_search":

            capability = get_capability(
                intent,
                target
            )

            if capability is None:

                result = {
                    "success": False,
                    "error": "Google Search capability is not registered."
                }

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result

            mission = Mission(
                goal=query
            )

            result = pipeline.run(
                capability,
                task,
                mission
            )

            print(result)

            update_state(
                "last_search",
                query
            )

            if not result["success"]:

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result
        # ---------------------------------
        # BROWSER (Runtime V2)
        # ---------------------------------

        elif intent == "browser":

            capability = get_capability(
                intent,
                target
            )

            if capability is None:

                result = {
                    "success": False,
                    "error": f"Browser capability '{target}' is not registered."
                }

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result

            mission = Mission(
                goal=query
            )

            result = pipeline.run(
                capability,
                task,
                mission
            )

            if not result["success"]:

                record_execution(
                    task,
                    result
                )

                record_strategy(
                    intent,
                    False
                )

                return result
#MOUSE

        elif intent == "mouse":

            if target == "move":

                result = move_mouse(
                    task["x"],
                    task["y"]
                )

            elif target == "click":

                result = left_click()

            elif target == "double_click":

                result = double_click()

            elif target == "right_click":

                result = right_click()

            else:

                result = {
                    "success": False,
                    "error": "Unknown mouse target"
                }

                return result
#KEYBOARD

        elif intent == "keyboard":

            if target == "type":

                result = type_text(
                    query
                )

            elif target == "enter":

                result = press_key(
                    "enter"
                )
            elif target == "hotkey":

                keys = query.split("|")

                result = hotkey(
                    *keys
                )

            else:

                result = {
                    "success": False,
                    "error": "Unknown keyboard target"
                }

                return result

#WINDOW

        elif intent == "window":

            if target == "focus":

                result = focus_window(query)

            elif target == "close":

                result = close_window(query)

            elif target == "minimize":

                result = minimize_window(query)

            elif target == "maximize":

                result = maximize_window(query)

            elif target == "list":

                result = list_windows()

            elif target == "active":

                result = get_active_window()

            else:

                result = {
                    "success": False,
                    "error": "Unknown window target"
                }

                return result
# SCREEN

        elif intent == "screen":

            if target == "click_text":

                result = click_text(
                    query
                )
            elif target == "double_click_text":

                result = double_click_text(
                    query
                )

            elif target == "right_click_text":

                result = right_click_text(
                    query
                )

            elif target == "type_at_text":

                parts = query.split(
                    "|",
                    1
                )

                if len(parts) != 2:

                    return {
                        "success": False,
                        "error": "Format: textbox|text"
                    }

                result = type_at_text(
                    parts[0],
                    parts[1]
                )

            else:

                result = {
                    "success": False,
                    "error": "Unknown screen target"
                }

                return result



        # ---------------------------------
        # UNKNOWN INTENT
        # ---------------------------------

        else:

            result = {

                "success": False,

                "error": f"Unknown intent: {intent}"
            }

            record_execution(
                task,
                result
            )

            record_strategy(
                intent,
                False
            )

            return result
                # ---------------------------------
        # CHECK ACTION RESULT
        # ---------------------------------

        if not result["success"]:

            record_execution(
                task,
                result
            )

            record_strategy(
                intent,
                False
            )

            return result


    except Exception as e:
        traceback.print_exc()


        result = {

            "success": False,

            "error": str(e)
        }

        record_execution(
            task,
            result
        )

        record_strategy(
            intent,
            False
        )

        return result


    # ---------------------------------
    # TELEMETRY
    # ---------------------------------

    duration = (

        time.time()

        - start_time
    )

    record_execution_time(

        intent,

        duration
    )


    # ---------------------------------
    # SUCCESS RESULT
    # ---------------------------------

    if "result" not in locals():

        result = {
            "success": True
        }

    task_to_store = (
        asdict(task)
        if is_dataclass(task)
        else task
    )

    update_state(
        "last_task",
        task_to_store
    )

    update_state(
        "last_result",
        result
    )

    record_execution(
        task,
        result
    )

    record_strategy(
        intent,
        True
    )

    return result