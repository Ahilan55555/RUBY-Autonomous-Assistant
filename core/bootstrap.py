import importlib
import os
import asyncio
from modules.memory.long_term_memory import load_memory
from core.lifecycle_manager import (

    register_plugin,

    set_plugin_state
)

from core.capability_registry_v2 import register_capability

from modules.capabilities.browser.search import (
    BrowserSearchCapability,
)
from modules.capabilities.browser.open_url import (
    BrowserOpenURLCapability,
)
from modules.capabilities.screen.actions import (
    ScreenCapability
)

loaded_plugins = []

PLUGIN_FOLDER = "modules/plugins"


def initialize_runtime():

    print("Initializing runtime...")
    load_memory()

    for filename in os.listdir(PLUGIN_FOLDER):
        if filename == "voice_plugin.py":
            continue

        if filename.endswith(".py") and not filename.startswith("__"):

            module_name = filename[:-3]

            module_path = f"modules.plugins.{module_name}"

            module = importlib.import_module(module_path)
            register_plugin(

                module_name
            )

            loaded_plugins.append(module)

            if hasattr(module, "register"):

                module.register()

            if hasattr(module, "initialize"):

                module.initialize()
                set_plugin_state(

                    module_name,

                    "active"
                )

            print(f"Loaded plugin: {module_name}")

    register_capability(
        intent="google_search",
        capability=BrowserSearchCapability(),
        purpose="Search Google using the browser.",
        limitations="Only searches Google.",
        examples=[
            "search python on google",
            "google AI news"
        ]
    )
    register_capability(

        intent="browser",

        target="search_google",

        capability=BrowserSearchCapability(),

        purpose="Search Google.",

        limitations="Requires browser access.",

        examples=[

            "search python on google",

            "google AI news"

        ]

    )
    register_capability(

        intent="browser",

        target="open_url",

        capability=BrowserOpenURLCapability(),

        purpose="Open any website URL in the browser.",

        limitations="Requires a valid website URL.",

        examples=[

            "open wikipedia.org",

            "open github.com",

            "open arxiv.org",

            "open https://example.com"

        ]
    )
    register_capability(

        intent="browser",

        target="search_youtube",

        capability=BrowserSearchCapability(),

        purpose="Search YouTube.",

        limitations="Requires YouTube.",

        examples=[

            "search music on youtube",

            "find robot videos"

        ]

    )

    register_capability(

        intent="browser",

        target="ask_chatgpt",

        capability=BrowserSearchCapability(),

        purpose="Send a prompt to ChatGPT.",

        limitations="Requires ChatGPT page.",

        examples=[

            "ask ChatGPT hello",

            "ask ChatGPT explain AI"

        ]

    )

    register_capability(

        intent="screen",

        target="scroll",

        capability=ScreenCapability(),

        purpose="Scroll the current screen up or down.",

        limitations="Requires a visible active application.",

        examples=[

            "scroll down",

            "scroll up",

            "scroll down the page",

            "scroll up the page"

        ]

    )
    register_capability(
        intent="screen",
        target="click_text",
        capability=ScreenCapability(),
        purpose="Click visible text identified using screen OCR.",
        limitations="Requires the requested text to be visible on screen.",
        examples=[
            "click the text box",
            "click Search",
            "click the Firefox button"
        ]
    )

    register_capability(
        intent="screen",
        target="double_click_text",
        capability=ScreenCapability(),
        purpose="Double-click visible text identified using screen OCR.",
        limitations="Requires the requested text to be visible on screen.",
        examples=[
            "double click the file",
            "double click Downloads"
        ]
    )

    register_capability(
        intent="screen",
        target="right_click_text",
        capability=ScreenCapability(),
        purpose="Right-click visible text identified using screen OCR.",
        limitations="Requires the requested text to be visible on screen.",
        examples=[
            "right click the folder",
            "right click Downloads"
        ]
    )

    register_capability(
        intent="screen",
        target="type_at_text",
        capability=ScreenCapability(),
        purpose="Find visible text using OCR, click it, and type text.",
        limitations="Requires the target text to be visible on screen.",
        examples=[
            "type hello into the search box",
            "type python into the text box"
        ]
    )

    print("Runtime V2 capabilities registered.")

    print("Runtime initialized.")




async def shutdown_runtime():

    print("Shutting down runtime...")

    for plugin in loaded_plugins:

        if hasattr(plugin, "shutdown"):

            shutdown_fn = plugin.shutdown
            plugin_name = (

                plugin.__name__

                .split(".")[-1]
            )


            set_plugin_state(

                plugin_name,

                "shutdown"
            )
            if asyncio.iscoroutinefunction(shutdown_fn):

                await shutdown_fn()

            else:

                shutdown_fn()