from gtts import gTTS
import winsound
import os
mytext = 'HELLO'
Greetings_morning = 'Good Morning! Aarthi'
language = 'en'

output = gTTS(text= mytext, lang = language, slow=False)
output.save("c:\src\output.mp3")
greetings_dict = {
"morning_aarthi": "Good Morning! Aarthi",
"morning_harish": "Good Morning! Harish",
}

for greetings in greetings_dict.keys():
    output = gTTS(text=greetings_dict[greetings], lang=language, slow=False)
    file = "c:\src\\"+greetings+".mp3"
    output.save(file)
    os.system("start "+file)



#os.system("mpg321 welcome.mp3")
os.system("start c:\src\output.mp3")
#filename='output.mp3'
#windsound.PlaySound(filename, winsound.SND_FILENAME)