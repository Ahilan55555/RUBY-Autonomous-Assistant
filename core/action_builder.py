from core.action import Action
from core.action_queue import ActionQueue


class ActionBuilder:

    def text_input(
        self,
        textbox,
        text
    ):

        queue = ActionQueue()

        queue.add(
            Action(
                action="click",
                target=textbox
            )
        )

        queue.add(
            Action(
                action="type",
                text=text
            )
        )

        queue.add(
            Action(
                action="wait",
                seconds=0.5
            )
        )

        queue.add(
            Action(
                action="press",
                key="enter"
            )
        )

        return queue

    def click(
        self,
        element
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="click",

                target=element

            )

        )

        return queue

    def click_and_type(
        self,
        element,
        text
    ):

        queue = ActionQueue()

        queue.add(
            Action(
                action="click",
                target=element
            )
        )

        queue.add(
            Action(
                action="type",
                text=text
            )
        )

        return queue

    def type(
        self,
        text
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="type",

                text=text

            )

        )

        return queue

    def press(
        self,
        key
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="press",

                key=key

            )

        )

        return queue

    def wait(
        self,
        seconds
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="wait",

                seconds=seconds

            )

        )

        return queue


    def hover(
        self,
        element
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="hover",

                target=element

            )

        )

        return queue


    def double_click(
        self,
        element
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="double_click",

                target=element

            )

        )

        return queue


    def right_click(
        self,
        element
    ):

        queue = ActionQueue()

        queue.add(

            Action(

                action="right_click",

                target=element

            )

        )

        return queue