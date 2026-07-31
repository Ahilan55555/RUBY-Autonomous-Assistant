class Capability:

    def prepare(
        self,
        step,
        mission
    ):
        pass

    def build_plan(
        self,
        step,
        mission
    ):
        raise NotImplementedError

    def execute(
        self,
        task,
        mission
    ):
        raise NotImplementedError

    def observe(self):
        return None

    def interpret(
        self,
        observation
    ):
        return observation

    


    def decide(
        self,
        interpretation,
        mission
    ):
        return interpretation


    def apply_result(
        self,
        mission,
        interpretation
    ):
        return interpretation


    def cleanup(
        self,
        mission
    ):
        pass