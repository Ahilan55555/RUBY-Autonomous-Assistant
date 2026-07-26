import time
from faster_whisper import WhisperModel

print("loading...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("loaded")

while True:

    start = time.time()

    
    segments, info = model.transcribe(
        "test.wav",
        language="en"
    )

    text = ""

    for segment in segments:
        text += segment.text

    print(text)

    print(
        "TRANSCRIBE:",
        time.time() - start
    )