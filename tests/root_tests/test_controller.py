import time
import asyncio

from core.agent_controller import (
    AgentController
)


async def main():

    controller = AgentController()

    start = time.time()

    await controller.process(
        "hello"
    )

    print(
        "\nTOTAL:",
        time.time() - start
    )


asyncio.run(main())