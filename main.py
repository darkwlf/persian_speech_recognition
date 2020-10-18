import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as micro:
   audio = r.listen(micro)
   said = ""


said = r.recognize_google(audio, language='fa-IR')
print(said)
