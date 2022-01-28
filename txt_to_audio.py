from gtts import gTTS
import os
from faker import Faker

fake = Faker()

name = fake.name()
email = fake.email()
country = fake.country()
profile = fake.profile()

mytext = f" My name is{name} I'm from {country}, You can send me message on email {email}, and hire is my profile{profile} "
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("/home/daniel/PycharmProjects/myprojects/welcome.mp3")