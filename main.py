import asyncio
from core.event_bus import (event_bus_worker , subscribe)
from core.router import handle_command
from core.monitor import system_monitor
from core.event_queue import event_worker
from modules.agents.monitor_agent import MonitorAgent
from modules.agents.goal_retry_agent import GoalRetryAgent
from core.bootstrap import (
    initialize_runtime,
    shutdown_runtime
)
import core.register_capabilities
from modules.llm.warmup import warmup_models



async def assistant_loop():

    while True:

        command = await asyncio.to_thread(input, ">>> ")

        if command == "exit":

            break

        await handle_command(command)



async def main():

    initialize_runtime()
    warmup_models()
    monitor_agent = MonitorAgent()

    subscribe(

        "execution",

        monitor_agent.handle_event
    )

    subscribe(

        "recovery",

        monitor_agent.handle_event
    )

    subscribe(

        "planning",

        monitor_agent.handle_event
    )

    retry_agent = GoalRetryAgent()

    retry_task = asyncio.create_task(

    retry_agent.retry_loop()
)

    event_bus_task = asyncio.create_task(

        event_bus_worker()
    )

    worker_task = asyncio.create_task(

        event_worker()
    )

    monitor_task = asyncio.create_task(

        system_monitor()
    )

    await assistant_loop()

    await shutdown_runtime()

    monitor_task.cancel()
    
    retry_task.cancel()

    worker_task.cancel()

    event_bus_task.cancel()

    print("Assistant shutting down...")

asyncio.run(main())
