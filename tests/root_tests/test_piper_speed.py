# test_piper_speed.py

import time

from modules.voice.tts import speak

start = time.time()

speak("Hello Ahilan")

print(
    time.time() - start
)