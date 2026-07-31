# test.py

from modules.perception.browser_observer import BrowserObserver


def test_browser_observer():

    observer = BrowserObserver()

    observation = observer.observe()

    print("\nButtons")
    print(observation.buttons)

    print("\nLinks")
    print(observation.links)

    print("\nHeadings")
    print(observation.headings)

    print("\nInputs")
    print(observation.inputs)

    print("\nPage Text")
    print(observation.page_text[:30])


if __name__ == "__main__":

    # Uncomment the test you want to run

    test_browser_observer()

    # test_goal_executor()

    # test_memory()

    # test_planner()

    # test_browser_search()

    # test_window_capture()