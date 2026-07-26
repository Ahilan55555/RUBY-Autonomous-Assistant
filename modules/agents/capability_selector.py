class CapabilitySelector:

    def choose(
        self,
        action,
        mission
    ):

        if action == "search":
            return "browser.search"

        if action == "read":
            return "browser.read_page"

        if action == "summarize":
            return "memory.summarize"

        if action == "save":
            return "files.save"

        if action == "play":
            return "browser.play"

        return None