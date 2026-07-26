from piper import PiperVoice
import wave

voice = PiperVoice.load(
    "voices/en_US-amy-medium.onnx"
)

with wave.open(
    "test.wav",
    "wb"
) as wav_file:

    voice.synthesize_wav(
        "Hello Ahilan",
        wav_file
    )

print("done")