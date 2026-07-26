# test_load_speed.py

import time
from piper import PiperVoice

start = time.time()

voice = PiperVoice.load(
    "voices/en_US-amy-medium.onnx"
)

print(
    "LOAD:",
    time.time() - start
)