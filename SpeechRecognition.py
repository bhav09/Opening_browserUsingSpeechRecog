# we will be taking a pass code and opening  google.com with Google API SpeechRecogniton

#dependencies
import speech_recognition as sr
import pyaudio
import webbrowser as wb

flag = 0
#an instance for recognizing the pass-code
r1 = sr.Recognizer()

#an instance for recognizing the voice taking you to the google.com
r2 = sr.Recognizer()

print('Speak the Pass code:)')
#accessing the default microphone
mic1 = sr.Microphone()
url = 'http://'
with mic1 as source:
    audio1 = r1.listen(source)
if r1.recognize_google(audio1) == 'hello world':
    flag = 1
#listening to the audio
if flag == 1:
    print(' Passcode accepted....!!')
    print('Ask for yourself:') #website where you want to go to.
    mic2 = sr.Microphone()
    with mic2 as source:
        audio2 = r2.listen(source)
        try:
            my_url = r2.recognize_google(audio2)
            print('You said:', my_url)
            wb.get().open_new(url+my_url)
            print('A new tab with ',my_url,' has opened in your browser..')
        except :
            print("Sorry couldn't make it")
else:
    print('Wrong pass-code')