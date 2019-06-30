import bs4
import urllib.request as url

for i in range(3):
    http = url.urlopen('https://www.flipkart.com/search?q=tv&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&page={}'.format(i+1))

    page = bs4.BeautifulSoup(http, 'lxml')

    divList = page.find_all('div', class_='_3wU53n')
    priceList = page.find_all('div', class_='_1vC4OE _2rQ-NK')
    #print(len(divList), len(priceList))
'''
    for i in range(len(divList)):
        print(divList[i].text)
        print(priceList[i].text)
        print("------------")
'''
    for item, price in zip(divList, priceList):
        print(item.text)
        print(price.text)
        print("------------")
