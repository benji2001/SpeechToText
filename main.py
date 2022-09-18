import speech_recognition as sr

filename = "preamble.wav"


# initialize the recognizer
ini = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = ini.record(source)
    # recognize (convert from speech to text)
    text = ini.recognize_google(audio_data)
    print(text)
