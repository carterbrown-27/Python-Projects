from gevent import monkey as curious_george
curious_george.patch_all(thread=False, select=False)
import requests
from lxml import html
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import datetime
import grequests

__author__ = 'Carter Brown'
__spec__  # gets price of mtg card buylist from kanatacg.com (Wizard's Tower)

totalPrice = 0.00

cardList = []

with open("list.txt") as f:
  for line in f:
    split = line.split("||")
    cardName= split[0]
    cardSet = split[1]
    isFoil = (split[2] == "Foil")
    cardList.append({'cardName':cardName, 'cardSet':cardSet, 'isFoil':isFoil})
# print(cardList)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://www.kanatacg.com/buylist',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}

domain = 'http://www.kanatacg.com/buylist/search'
reqs = []

for card in cardList:
    params = (
        ('query', card['cardName']),
    )
    reqs.append(grequests.get(domain, headers=headers, params=params))

# makes async requests, stores responses in order sent (map)
# this was approx 5x faster for a set of 14 cards. (approx 2.4s vs approx 12s)
responses = grequests.map(reqs)
# print(responses)

count = 0
for response in responses:
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.findAll('td',attrs={'width':'100%','valign':'top'})
    # results = soup.find_all('small')
    # print(results)

    card = cardList[count]
    price = 0.00
    for result in results:
        # print(type(result))
        s = result.small.text
        if card['cardName'] not in result.a.text: continue
        # print(s)
        if s.lower() != card['cardSet'].lower(): continue
        #print("correct set")
        foil = 'Foil' in result.a.text
        if foil!=card['isFoil'] : continue

        # if right card, set, foiling
        p = result.table.tr.td.next_sibling.next_sibling
        p = p.text[5:]
        print(card['cardName'] + ": " + p)
        price = float(p)
        if price == 0.00: print(card['cardName']+": X")
        totalPrice += price
    count+=1

print("$"+str(round(totalPrice,2)))
finalBonusPrice = str(round(totalPrice*1.15,2))
print("w/ Store Credit Bonus = $"+finalBonusPrice)

with open("history.txt", 'a') as w:
  w.write(str(datetime.date.today()) +": $"+finalBonusPrice+"\n")
