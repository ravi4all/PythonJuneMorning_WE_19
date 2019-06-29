Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Chat_5.py 
Enter your name : Ram
Hello Ram
Enter your message : hi
Hello Ram
Enter your message : hello
Hello Ram
Enter your message : bye
Bye Ram, See you soon
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 6, 29, 10, 51, 42, 781660)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 6, 29, 10, 52, 55, 831468)
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2019, 6, 29, 10, 53, 20, 489542)
>>> print(dt.now())
2019-06-29 10:53:52.635247
>>> d = dt.now().date()
>>> print(d)
2019-06-29
>>> d.strftime('%d/%m/%y,%a')
'29/06/19,Sat'
>>> t = dt.now().time()
>>> t
datetime.time(10, 55, 10, 986992)
>>> print(t)
10:55:10.986992
>>> t.strftime('%H:%M:%S:%p')
'10:55:10:AM'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Chat_5.py 
Enter your name : Ram
Hello Ram
Enter your message : hi
Hello Ram
Enter your message : hello
Hello Ram
Enter your message : date please
29/06/19,Sat
Enter your message : time please
10:59:19,AM
Enter your message : bye
Bye Ram, See you soon
>>> import webbrowser
>>> webbrowser.open('google.com')
True
>>> msg = "open youtube"
>>> msg.split()
['open', 'youtube']
>>> msg = "please open youtube"
>>> msg = "open youtube please"
>>> msg.split()
['open', 'youtube', 'please']
>>> msg = "open youtube"
>>> msg.split()[-1]
'youtube'
>>> web = msg.split()[-1]
>>> webbrowser.open(web+'.com')
True
>>> websites = {"youtube":"youtube.com","google":"google.com","wikipedia":"wikipedia.org"}
>>> from googlesearch.googlesearch import GoogleSearch
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    from googlesearch.googlesearch import GoogleSearch
  File "C:\Python37\lib\site-packages\googlesearch\googlesearch.py", line 6, in <module>
    import urllib2
ModuleNotFoundError: No module named 'urllib2'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Chat_5.py 
Enter your name : Ram
Hello Ram
Enter your message : hi
Hello Ram
Enter your message : hello
Hello Ram
Enter your message : date please
29/06/19,Sat
Enter your message : open facebook
Enter your message : bye
Bye Ram, See you soon
>>> import os
>>> os.system('calc')
0
>>> os.getcwd()
'C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\2019\\June\\Python_WE_June_2'
>>> os.chdir("C:\Users\asus\Music")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir(r"C:\Users\asus\Music")
>>> os.listdir()
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'desktop.ini', 'Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg', 'Galti.mp3', 'Kaththi Theme…The Sword of Destiny - Full Audio.ogg', 'music_1.ogg', 'Na Ja.mp3', 'Shape of You.mp3', 'Street Fighter V Soundtrack - Main Menu.ogg', "Street Fighter V Soundtrack - Ryu's Theme.ogg", 'StreetFighter.mp3', 'Top 10 Tamil Mass BGM (Theme Song) 2011-2016.mp4', 'Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg']
>>> songs = os.listdir()
>>> import random
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> os.startfile(song)
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> import glob
>>> songs = glob.glob('*.mp3')
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> songs
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'Galti.mp3', 'Na Ja.mp3', 'Shape of You.mp3', 'StreetFighter.mp3']
>>> songs = glob.glob('*.mp3') + glob.glob('*.ogg')
>>> songs
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'Galti.mp3', 'Na Ja.mp3', 'Shape of You.mp3', 'StreetFighter.mp3', 'Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg', 'Kaththi Theme…The Sword of Destiny - Full Audio.ogg', 'music_1.ogg', 'Street Fighter V Soundtrack - Main Menu.ogg', "Street Fighter V Soundtrack - Ryu's Theme.ogg", 'Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg']
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Chat_5.py 
Enter your name : Ram
Hello Ram
Enter your message : hi
Hello Ram
Enter your message : play song
Enter your message : bye
Bye Ram, See you soon
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Chat_5.py 
Enter your name : Ram
Hello Ram
Enter your message : hi
Hello Ram
Enter your message : show songs
5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3
BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3
Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3
Galti.mp3
Na Ja.mp3
Shape of You.mp3
StreetFighter.mp3
Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg
Kaththi Theme…The Sword of Destiny - Full Audio.ogg
music_1.ogg
Street Fighter V Soundtrack - Main Menu.ogg
Street Fighter V Soundtrack - Ryu's Theme.ogg
Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg
Which song you want to play : bye
Enter your message : 
I don't understand
Enter your message :  bye
I don't understand
Enter your message : bye
Bye Ram, See you soon
>>> songs
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'Galti.mp3', 'Na Ja.mp3', 'Shape of You.mp3', 'StreetFighter.mp3', 'Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg', 'Kaththi Theme…The Sword of Destiny - Full Audio.ogg', 'music_1.ogg', 'Street Fighter V Soundtrack - Main Menu.ogg', "Street Fighter V Soundtrack - Ryu's Theme.ogg", 'Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg']
>>> for i in range(len(songs)):
	print(i,songs[i])

	
0 5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3
1 BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3
2 Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3
3 Galti.mp3
4 Na Ja.mp3
5 Shape of You.mp3
6 StreetFighter.mp3
7 Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg
8 Kaththi Theme…The Sword of Destiny - Full Audio.ogg
9 music_1.ogg
10 Street Fighter V Soundtrack - Main Menu.ogg
11 Street Fighter V Soundtrack - Ryu's Theme.ogg
12 Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg
>>> for index,song in enumerate(songs):
	print(index,song)

	
0 5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3
1 BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3
2 Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3
3 Galti.mp3
4 Na Ja.mp3
5 Shape of You.mp3
6 StreetFighter.mp3
7 Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg
8 Kaththi Theme…The Sword of Destiny - Full Audio.ogg
9 music_1.ogg
10 Street Fighter V Soundtrack - Main Menu.ogg
11 Street Fighter V Soundtrack - Ryu's Theme.ogg
12 Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg
>>> for index,song in enumerate(songs,start=1):
	print(index,song)

	
1 5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3
2 BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3
3 Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3
4 Galti.mp3
5 Na Ja.mp3
6 Shape of You.mp3
7 StreetFighter.mp3
8 Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg
9 Kaththi Theme…The Sword of Destiny - Full Audio.ogg
10 music_1.ogg
11 Street Fighter V Soundtrack - Main Menu.ogg
12 Street Fighter V Soundtrack - Ryu's Theme.ogg
13 Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg
>>> songs[1]
'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3'
>>> songs[1 - 1]
'5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Chat_5.py 
Enter your name : Ram
Hello Ram
Enter your message : hi
Hello Ram
Enter your message : show songs
1 5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3
2 BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3
3 Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3
4 Galti.mp3
5 Na Ja.mp3
6 Shape of You.mp3
7 StreetFighter.mp3
8 Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg
9 Kaththi Theme…The Sword of Destiny - Full Audio.ogg
10 music_1.ogg
11 Street Fighter V Soundtrack - Main Menu.ogg
12 Street Fighter V Soundtrack - Ryu's Theme.ogg
13 Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg
Which song you want to play : 8
Enter your message : bye
Bye Ram, See you soon
>>> import json
>>> import urllib.request as url
>>> data = json.load(url.urlopen("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=695e07af402f4b119f0703e9b19f4683"))
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['status', 'totalResults', 'articles'])
>>> data['totalResults']
10
>>> articles = data['articles']
>>> article = articles[0]
>>> article.keys()
dict_keys(['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'])
>>> article['title']
'A rare glimpse into the sweeping -- and potentially troubling  -- cloud kitchens trend'
>>> for i in range(data['totalResults']):
	article = articles[i]
	print(article['title'])

	
A rare glimpse into the sweeping -- and potentially troubling  -- cloud kitchens trend
Google finance head joins Postmates board ahead of anticipated IPO
SpaceX aims to provide commercial Starship launches by 2021
Theranos founder Elizabeth Holmes to stand trial in 2020
Check out the breakout sessions at TC Sessions: Mobility
Facebook SDK bug crashes apps like Timehop
Happy weekend, Slack is down for real this time
Tesla's in-dash sketchpad software is getting better in the next system update
Apple tries out the 'choose-your-own adventure' Twitter thread format that recently went viral
3D manufacturer Carbon helps customers scale polymer products – TechCrunch
>>> 
