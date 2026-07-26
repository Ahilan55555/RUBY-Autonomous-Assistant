from modules.perception.browser_observer import BrowserObserver

observer = BrowserObserver()

observation = observer.observe()

print("\nButtons\n")

print(observation.buttons)

print("\nLinks\n")

print(observation.links)

print("\nHeadings\n")

print(observation.headings)

print("\nInputs\n")

print(observation.inputs)

print("\nPage Text\n")

print(observation.page_text[:30])