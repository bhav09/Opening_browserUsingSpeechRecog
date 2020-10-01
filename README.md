# Opening_browserUsingSpeechRecog
It includes dependencies like pyaudio , webbrowser , speechrecognition

#Installing the packages:

->webbrowser is inbuilt

->pip install pyaudio
Some people face problem in installing PyAudio so you can visit this website and install externally
Website : https://www.lfd.uci.edu/~gohlke/pythonlibs/
Search for PyAudio and install according to your python version and os configuration.

->pip install speechrecognition

1. This program asks for a Specific pass code that you have to speak


2. The spoken word(s) hence will be recognized by recognizer class


3. If it matches with the required passcode .
      
            3.1 You will be asked to speak the website where you want to go.
      
            3.2 A new tab will be opened in your browser with your desired url.
   
   Else throws a default wrong pass code message
   
   
References :

https://www.quora.com/How-do-I-open-a-URL-in-Google-Chrome-in-new-tab-using-Python
https://realpython.com/python-speech-recognition/
