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

    def collect_result(
        self,
        mission,
        observation
    ):
        return observation

    def cleanup(
        self,
        mission
    ):
        pass