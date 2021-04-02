from gtts import gTTS
import os

import speech_recognition as sr

voice= "female"


def handle_text_from_spr(text):
    language = 'en'
    you_said= 'You  said '
    text_file = you_said + text
    output = gTTS(text=text_file, lang=language, slow=False)
    file = "c:\src\\" + text + ".mp3"
    output.save(file)
    os.system("start " + file)



while True:
    print('listening....')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print('You Said='+text)
            handle_text_from_spr(text)
            if text == "stop":
                break



            voice = voice + str(text)
        except:
            print(' unable to decode, say sometthing.... ')

hr = gTTS(text=voice, lang='en', slow=False)
hr.save("1.wav")


