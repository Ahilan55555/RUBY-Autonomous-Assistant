class CapabilitySelector:

    def choose(
        self,
        mission_step,
        goal_context
    ):

        if mission_step == "search":
            return "browser.search"

        return None