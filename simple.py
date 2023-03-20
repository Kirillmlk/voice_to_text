import os
import wave

from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(0)

if not os.path.exists("vosk-model-ru"):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack")
    exit(1)


def main() -> None:
    wf = wave.open('stream_voice_to_text.wav', "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit(1)

    model = Model("vosk-model-ru")
    rec = KaldiRecognizer(model, wf.getframerate())
    with open('voice_to_text.txt', 'w', encoding='utf-8') as file:
        while True:
            date = wf.readframes(4000)
            if len(date) == 0:
                break
            if rec.AcceptWaveform(date):
                print("###", rec.Result())
            else:
                print(rec.PartialResult())


main()
