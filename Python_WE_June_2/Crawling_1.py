import bs4
import urllib.request as url

http = url.urlopen('https://www.flipkart.com/search?q=tv&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY')
print(http)

page = bs4.BeautifulSoup(http, 'lxml')
#div = page.find('div', class_='_3wU53n')
#print(div.text)

divList = page.find_all('div', class_='_3wU53n')
for item in divList:
    print(item.text)
