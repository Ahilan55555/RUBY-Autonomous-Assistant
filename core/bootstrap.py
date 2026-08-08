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