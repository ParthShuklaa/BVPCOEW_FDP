#Step1: Import Packages
import os
import gtts
from gtts import gTTS

#Step2: Creating instance/object
myText = "Thank you for inviting me as " \
         "a speaker for Faculty Development program "

myvoice = gTTS(text=myText,lang='en',slow=False)
#Step3: Saving it as Mp3
myvoice.save("Voice.mp3")
#Step4: Playing my audio file
os.system("Voice.mp3")
