import pyttsx3 as ttx
from vosk import Model, KaldiRecognizer
import pyaudio
import json

assistant = ttx.init()
voice = assistant.getProperty("voices")
assistant.setProperty("voice", "french")


model = Model("assets/model/vosk-model-small-fr-0.22")
rec = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)


def talk(text):
    if (text == ""):
        pass
    else:
        print("Bot:", text)
        assistant.say(text)
        assistant.runAndWait()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)
            # si je ne parle pas
            if (result["text"] == ""):
                pass
            print("Moi:", result['text'])
            return result['text']
