import bs4
import urllib.request as url

path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="
movieName = input("Enter Movie Name : ")
movieName = movieName.split()
movieName = '+'.join(movieName)
http = url.urlopen(path+movieName)

page = bs4.BeautifulSoup(http, 'lxml')
td = page.find('td', class_='result_text')
a_tag = td.find('a')
href = a_tag['href']
newPath = "https://www.imdb.com" + href

http = url.urlopen(newPath)
page = bs4.BeautifulSoup(http, 'lxml')
title = page.find('div', class_='title_wrapper')
title = title.text.replace('\n','')
title = ' '.join(title.split())
print(title)
