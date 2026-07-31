from modules.perception.browser_observer import BrowserObserver


def main():

    observer = BrowserObserver()

    observation = observer.observe()

    print("\n========== BUTTONS ==========\n")
    print(observation.buttons)

    print("\n========== LINKS ==========\n")
    print(observation.links)

    print("\n========== HEADINGS ==========\n")
    print(observation.headings)

    print("\n========== INPUTS ==========\n")
    print(observation.inputs)

    print("\n========== PAGE TEXT ==========\n")
    print(observation.page_text[:30])

    print("\n========== TOTALS ==========\n")
    print(f"Buttons : {len(observation.buttons)}")
    print(f"Links   : {len(observation.links)}")
    print(f"Headings: {len(observation.headings)}")
    print(f"Inputs  : {len(observation.inputs)}")
    print(f"PageTxt : {len(observation.page_text)}")
    print(f"Visible : {len(observation.visible_text)}")


if __name__ == "__main__":
    main()