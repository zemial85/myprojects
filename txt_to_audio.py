from gtts import gTTS
import os

mytext = "Ewa chce komputer, który gada"

language = 'pl'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("/home/daniel/PycharmProjects/myprojects/welcome.mp3")