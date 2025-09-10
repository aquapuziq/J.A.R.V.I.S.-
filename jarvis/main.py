import speech_recognition
import os
import pyttsx3
import subprocess

class JarvisHead:
    name = ""
    sex = ""
    speechLang = ""
    recognitionLang = ""

def recognizeAudio(*args: tuple):
    with micro:
        recognizedData = ""
        recognizer.adjust_for_ambient_noise(micro, duration = 2)

        audio = recognizer.listen(micro, 3 ,3)

        with open("microphone-results.wav", "wb") as file:
            file.write(audio.get_wav_data())

        recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        return recognized_data


if __name__ == '__main__':
    recognizer = speech_recognition.Recognizer()
    micro = speech_recognition.Microphone()

    jarvisTts = pyttsx3.init()

    assistant = JarvisHead()
    assistant.name = "JARVIS"
    assistant.sex = "male"
    assistant.speech_language = "ru"

    while True:
        voiceInput = recognizeAudio()
        os.remove("microphone-results.wav")
        print(voiceInput)

        voiceInput = voiceInput.split(" ")
        command =" ".join(voiceInput[:3])

        if command == "джарвис запусти танки":
            jarvisTts.runAndWait()
            subprocess.Popen(r'C:\steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe', shell = True)




