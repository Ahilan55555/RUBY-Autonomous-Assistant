from modules.llm.classifier_client import classify
import time

start = time.time()

print(
    classify(
        "hi"
    )
)

print(
    time.time() - start
)