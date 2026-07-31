from core.logger import log_action, log_error
from core.parser import parse_command
from modules.memory.session_memory import save_command
from core.event_queue import event_queue
from modules.memory.experience_manager import (

    store_experience
)

from core.handlers import (
    handle_create_folder,
    handle_delete_folder,
    handle_google_search,
    handle_terminal_command,
    handle_history,
    handle_open_last_folder,
    handle_reminder
)

from modules.automation.apps import (
    open_firefox,
    open_sublime
)

from modules.automation.browser import (
    open_youtube,
    open_github,
    
)
from modules.actions.file_actions import (
    create_file,
    open_file
)

from modules.automation.files import (
    
    list_files
)

from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from core.intent_executor import (
    execute_intent
)

from modules.agents.response_agent import (
    ResponseAgent
)
from modules.agents.chat_agent import (
    ChatAgent
)
from modules.voice.tts import speak



from modules.actions.desktop_actions import (
    open_terminal,
    open_chatgpt
)
from core.file_handlers import (
    handle_create_file,
    handle_open_file,
    handle_read_file
)
from core.code_handlers import (
    handle_run_python
)

import time
import threading

chat_agent = ChatAgent()


COMMAND_WORDS = [
    "open",
    "close",
    "search",
    "run",
    "create",
    "delete",
    "list",
    "show",
    "remind"
]
# Fixed commands
COMMANDS = {
    "open terminal": open_terminal,

    "open chatgpt": open_chatgpt,

    "open firefox": open_firefox,

    "open sublime": open_sublime,

    "open youtube": open_youtube,

    "open github": open_github,

    "list files": list_files,

    "history": lambda: handle_history("history", []),

    "open last folder": lambda: handle_open_last_folder("", [])


}





# Parsed command registry
PARSED_COMMANDS = {
    
    "run terminal": handle_terminal_command,

    "create folder": handle_create_folder,

    "delete folder": handle_delete_folder,

    "search google": handle_google_search,

    "create file": handle_create_file,

    "open file": handle_open_file,

    "read file": handle_read_file,

    "run python": handle_run_python,

    "remind me": handle_reminder
}


async def handle_command(command):

    try:

        command = command.strip()

        if not command:
            return

        save_command(command)

        store_experience(command)

        command_lower = command.lower()


        parsed = parse_command(
            command_lower
        )

        # -------------------------
        # Grammar Commands
        # -------------------------

        if isinstance(parsed, dict) and "handler" in parsed:

            await event_queue.put(

                (
                    5,
                    {
                        "type": "command",
                        "command": command_lower,
                        "handler": parsed["handler"],
                        "args": parsed["args"]
                    }
                )
            )

            return

        # -------------------------
        # Safe Extraction
        # -------------------------

        verb = parsed.get(
            "verb",
            ""
        )

        target = parsed.get(
            "target",
            ""
        )

        args = parsed.get(
            "args",
            []
        )

        command_key = (
            f"{verb} {target}"
            .strip()
        )

        # -------------------------
        # Fixed Commands
        # -------------------------

        if command_lower in COMMANDS:

            log_action(
                command_lower
            )

            await event_queue.put(

                (
                    5,
                    {
                        "type":
                        "fixed_command",

                        "command":
                        command_lower,

                        "handler":
                        COMMANDS[
                            command_lower
                        ]
                    }
                )
            )

            return

        # -------------------------
        # Parsed Commands
        # -------------------------

        if command_key in PARSED_COMMANDS:

            await event_queue.put(

                (
                    5,
                    {
                        "type":
                        "command",

                        "command":
                        command_lower,

                        "handler":
                        PARSED_COMMANDS[
                            command_key
                        ],

                        "args":
                        args
                    }
                )
            )

            return

        # -------------------------
        # Planner Fallback
        # -------------------------
        # -------------------------
        # Planner Fallback
        # -------------------------

        planner = AdaptivePlanner()

        plan = planner.recover(
            command
        )
        print(
            f"[PLAN TASKS] {len(plan.tasks)}"
        )
        if plan.goal == "unsupported":

            print("\nAssistant:\n")

            print(
                "I don't currently support that action."
            )

            return
            
        if not plan.tasks:

            start = time.time()

            reply = chat_agent.reply(
                command
            )

            print(
                "\nAssistant:\n"
            )

            print(
                reply
            )

            threading.Thread(
                target=speak,
                args=(reply,),
                daemon=True
            ).start()

            print(
                f"\nTIME: {time.time() - start:.2f}s"
            )

            return


        

        response_agent = (
            ResponseAgent()
        )

        if not plan:

            print(
                "\nAssistant:"
            )

            print(
                "I could not create a plan."
            )

            return

        for step in plan.tasks:

            result = execute_intent(
                step
            )

            response = (
                response_agent
                .respond(result)
            )

            print(
                "\nAssistant:"
            )

            print(
                response
            )
            threading.Thread(
                target=speak,
                args=(response,),
                daemon=True
            ).start()

    except Exception as e:

        print(
            f"Error: {e}"
        )

        log_error(
            str(e)
        )