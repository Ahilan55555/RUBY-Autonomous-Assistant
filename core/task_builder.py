from core.task import Task

from core.action_builder import ActionBuilder


class TaskBuilder:

    def __init__(self):

        self.actions = ActionBuilder()


    def text_input(
        self,
        textbox,
        text
    ):

        queue = self.actions.text_input(

            textbox,

            text

        )

        return Task(

            name="Text Input",

            action_queue=queue

        )

    def click(
        self,
        element
    ):

        return Task(

            name="Click",

            action_queue=self.actions.click(
                element
            )

        )

    def type(
        self,
        text
    ):

        return Task(

            name="Type",

            action_queue=self.actions.type(
                text
            )

        )

    def press(
        self,
        key
    ):

        return Task(

            name="Press",

            action_queue=self.actions.press(
                key
            )

        )


    def wait(
        self,
        seconds
    ):

        return Task(

            name="Wait",

            action_queue=self.actions.wait(
                seconds
            )

        )

    def hover(
        self,
        element
    ):

        return Task(

            name="Hover",

            action_queue=self.actions.hover(
                element
            )

        )

    def double_click(
        self,
        element
    ):

        return Task(

            name="Double Click",

            action_queue=self.actions.double_click(
                element
            )

        )


    def right_click(
        self,
        element
    ):

        return Task(

            name="Right Click",

            action_queue=self.actions.right_click(
                element
            )

        )

    def search(
        self,
        textbox,
        query
    ):

        queue = self.actions.text_input(

            textbox,

            query

        )

        return Task(

            name="Search",

            action_queue=queue,

            parameters={

                "query": query

            }

        )