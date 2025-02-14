import speech_recognition as sr
from gtts import gTTS
import os

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio):
        try:
            return self.recognizer.recognize_google(audio, language='en-US')
        except sr.UnknownValueError:
            return None

    def synthesize_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('output.mp3')
        os.system('start output.mp3')
