from datetime import datetime as dt
import webbrowser
import glob, os, random

name = input("Enter your name : ")
print("Hello",name)

helloIntent = ["hi","hello","hey","hi there","hey there","howdy"]
timeIntent = ["time please","what's the time","please tell me time","tell me time"]
dateIntent = ["date please","today's date","what's the date today","tell me date"]
musicIntent = ["play music","play song","start song","start music"]

while True:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello",name)
    elif msg in timeIntent:
        currentTime = dt.now().time()
        print(currentTime.strftime("%H:%M:%S,%p"))
    elif msg in dateIntent:
        date = dt.now().date()
        print(date.strftime("%d/%m/%y,%a"))
    elif msg.startswith('open'):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg in musicIntent:
        os.chdir(r"C:\Users\asus\Music")
        songs = glob.glob('*.mp3') + glob.glob('*.ogg')
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "show songs":
        os.chdir(r"C:\Users\asus\Music")
        songs = glob.glob('*.mp3') + glob.glob('*.ogg')
        for index,song in enumerate(songs,start=1):
            print(index,song)
        songNum = int(input("Which song you want to play : "))
        os.startfile(songs[songNum - 1])
    elif msg == "bye":
        print("Bye {}, See you soon".format(name))
        break
    else:
        print("I don't understand")
