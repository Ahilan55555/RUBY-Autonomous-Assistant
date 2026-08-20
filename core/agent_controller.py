import time
import threading

from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from modules.agents.chat_agent import (
    ChatAgent
)

from modules.agents.response_agent import (
    ResponseAgent
)

from core.intent_executor import (
    execute_intent
)

from modules.voice.tts import (
    speak
)


class AgentController:
    
    def __init__(self):

        self.chat = ChatAgent()

        self.planner = AdaptivePlanner()

        self.response_agent = (
            ResponseAgent()
        )

    async def process(

        self,

        command
    ):
        
        chat_starters = [

            "hello",
            "hi",
            "hey",
            "how are you",
            "what is",
            "who is",
            "why",
            "how",
            "tell me"
        ]

        if any(
            command.lower().startswith(x)
            for x in chat_starters
        ):

            reply = self.chat.reply(
                command
            )

            print(
                "\nAssistant:\n"
            )

            print(reply)

            return

        plan = self.planner.recover(
            command
        )
        # Runtime V2 capabilities are validated
        # by the capability registry / executor.
        #
        # Do not maintain a second hard-coded
        # supported-intents list here.

        

        if not plan.tasks:

            start = time.time()

            chat = ChatAgent()

            reply = chat.reply(
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

        

        for task in plan.tasks:

            result = execute_intent(
                task
            )

            response = (
                self.response_agent
                .respond(result)
            )

            print(
                "\nAssistant:\n"
            )

            print(
                response
            )

            speak(response)