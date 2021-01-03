from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good night")

    speak("I am Mellisa,Your voice assistant Sir. Please tell me how may I help you")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.MELISSA()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def MELISSA(self):
        wish()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open stackoverflow' in self.query:
                speak("opening stackoverflow for you...")
                webbrowser.open("stackoverflow.com")   


            elif 'open codeblocks' in self.query:
                speak("opening codeblocks for you...")
                codeblocksPath = "C:\\Users\\VAIBHAV SHARMA\\Desktop\\Programing\\CodeBlocks\\codeblocks.exe"
                os.startfile(codeblocksPath)

            elif 'open Chandigarh university managemnet system' in self.query:
                speak("opening Chandigarh university managemnet system for you...")
                webbrowser.open("https://uims.cuchd.in/uims/")

            elif 'open blackboard' in self.query:
                speak("opening blackboard for you...")
                webbrowser.open("https://cuchd.blackboard.com/")

            elif 'what is the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:

                speak("open vs codes for you...")  
                codePath = "C:\\Users\\VAIBHAV SHARMA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to vaibhav' in self.query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "yovaibhav43@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")  

            elif 'play game' in self.query:
                speak("7 up Game You have to guess if the sum of two dice is below seven above seven or if lucky seven")
                max=6
                min=1
                account=0
                speak("enter your bidding amount")
                credit=takeCommand()
                speak("choice 1 seven Up")
                speak("choice 2 Equals seven")
                speak("choice 3 seven Down")
                        
                a=random.randint(min,max)
                b=random.randint(min,max)
                c=a+b
                speak("Enter Your Choice")
                ch = takeCommand()
                print("Dice is rolling...")
                print("The answer is %d",c)
                if(ch==1):
                    if(c>7):
                        account=account+credit*2
                        speak("Congrats! You won\n")
                    else:
                        account=account-credit
                        speak("Sorry You Lose\n")

                elif(ch==2):
                    if(c==7):
                        speak("Sorry You Lose\n")


                elif(ch==3):
                    if(c<7):
                        account=account+credit*2 
                        speak("Conrats! You won\n")
                    else:
                        account=account-credit
                        speak("Sorry You Lose\n")

                else:
                    speak("wrong input")
                    print("The balance is %d",account)
                    speak("do you want to play more")

                a=takeCommand().upper()
            elif 'calculate' in self.query:
                

                r = sr.Recognizer()
                my_mic_device = sr.Microphone()

                with my_mic_device as source:
                    speak("say what do you want to calculate, example two plus four")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)


                my_string=r.recognize_google(audio)
                speak(my_string)
                def get_operator_fn(op):

                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                    speak(eval_binary_expr(*(my_string.split())))  
    









FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())