import pyttsx3
import speech_recognition as sr
import pyaudio
import random
import os

engine = pyttsx3.init()

def speak(text):
	engine.say(text)
	engine.runAndWait()
speak('welcome')
def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('say somthing:')
		a = r.listen(source)
		try:
			print ("you said:" + r.recognize_google(a))
		
		except sr.UnknownValueError:
			print('could not understand audio')

		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		
		return ""

def media():
	speak('how you doing?')
	speak('starting required application..')
	speak('which song should i play for you?')
	k = listen()
	speak('ok dude playing'+k+ 'sure')
	os.startfile('Vanessa_Carlton_-_A_Thousand_Miles.mp3')

def shutdown():
	speak('understood sir')
	speak('connecting to command prompt')
	speak('shuttingdown your computer')
	os.system("shutdown -r -t 1")

def gooffline():
	speak('hello')
	speak('closing all systems')
	speak('disconnecting to servers')
	speak('going offline')
	speak('bye dude')
	quit()

def online():
	speak("hello")
	speak("im cortex. welcome to my world")
	speak("im ready")
	os.system('hi_tech.rmskin')
"""def logout():
	speak('logging off')
	speak("current user")
	os.system(""shutdown -t 0 -l"")"""

def mainfunction():
	a = r.listen(source)
	user = r.recognize_google(a)
	print(user)

	if user == "cortex":
		online()
	elif user == "song":
		media()
	elif user== "down":
		gooffline()
	elif user == "shutdown":
		shutdown()
	#elif user == "logout":
	#	logout()
	elif user in ['hi','hello','hey']:
		d = random.choice(['hey','hi','supp'])
		speak(d)
	elif user == "what are you doing":
		speak('nothing. just chilling')

if __name__=="__main__":
	r = sr.Recognizer()
	with sr.Microphone() as source:
		for x in xrange(1,10):
			mainfunction()