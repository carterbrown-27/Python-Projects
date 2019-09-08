__author__ = "Carter Brown"
""" scrapes data from past horse races from timeformus.com, avgs it, and formats the results in Markdown.
With an account, (or just steal mine I guess, not important enough to hash it :P) find a Free PPS race (or a purchased race)
and grab the raceID, found as the last 6 (as of 09/2019) digits in the URL & enter it when prompted. """

import requests
from lxml import html
import time
from bs4 import BeautifulSoup
from datetime import timedelta
from html.parser import HTMLParser
import json
# names: id="pp-horse-data"
# id="pp-horse-name"
# click = onShowWorkoutDetail(e)

# login

session_requests = requests.session()
login_url = "https://timeformus.com/login?ReturnUrl=/"
result = session_requests.get(login_url)

soup = BeautifulSoup(result.content, "html.parser")
#print(soup)

tokenz = soup.find_all("input",type="hidden")
#print(tokenz)

for token in tokenz:
  value = token['value']
  break

print("=====")

print("<testing> remember to input username and pw")
raceID = input("Enter the RaceID, and hit ENTER: ") # input here
url = "https://timeformus.com/basicpps/" + str(raceID)

# login payload
""" Enter Your Login Info Here """
payload = {
  "UserName": "carterTest27", # input username here
  "Password": "ughhXY7Fts7fDtq",  # input password here
  "__RequestVerificationToken": value,
  "returnUrl": "/basicpps/" + str(raceID)
}

result = session_requests.post(
  login_url,
  data = payload,
  headers = dict(referer=login_url)
)

# print(result.ok)
f = open("doc.md","w")
r = session_requests.get(url)

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; CrOS aarch64 12239.44.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.68 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'none',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = session_requests.get('https://timeformus.com/basicpps/'+str(raceID), headers=headers)
trackDataSoup = BeautifulSoup(response.content, "html.parser")
# print(trackDataSoup)
trackData = trackDataSoup.findAll('option', attrs={"selected":"selected"})

print(trackData[0].text+"| "+trackData[1].text+" | "+trackData[2]['data-display'])
print("=====")
f.write("## **"+trackData[0].text+" | "+trackData[1].text+" | "+trackData[2]['data-display']+"** \n")

soup = BeautifulSoup(r.content,"html.parser")
#print(soup)

headers = {
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (X11; CrOS aarch64 12239.44.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.68 Safari/537.36',
    'Accept': 'html, */*',
    'Referer': url,
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('raceId', raceID),
    ('_', time.time()),
)

# race details request
response = session_requests.get('https://timeformus.com/raceinfo/racedetails', headers=headers, params=params)

raceDetails = str(response.content)[2:-1]
raceDetails = json.loads(raceDetails)

horseNum = 1
for horse in raceDetails:
  # print(horse)
  starterID = horse['StarterID']
  # print(starterID)

  # horsename
  horseName = soup.find(attrs={"data-id":starterID})['data-name']
  f.write("# ")
  if horse['Scratch']:
    print("(scr)")
    f.write("~~")
  nameAndNum = str(horseNum) + ". " + horseName
  print(nameAndNum)
  f.write("**"+nameAndNum+"**")
  if horse['Scratch']:
    f.write("~~")
  f.write("\n")

  horseNum += 1

  headers = {
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html, */*; q=0.01',
    'Referer': url,
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
  }

  params = (
  ('starterId', starterID),
  )

  # workout request
  workout_details = session_requests.get('https://timeformus.com/basicpps/starterWorkouts', headers=headers, params=params)
  # print(workout_details.ok)

  workout_soup = BeautifulSoup(workout_details.content,"html.parser")
  # print(soup)

  session_requests.close();

  items = workout_soup.find(id="workouts").findAll('li')
  # print(items)

  lastFive = []
  x = 0
  for item in items:
    if x>=5:
      break

    stats = item.span.next_sibling.string
    # print(stats)

    index = stats.find("Race")
    if index != -1:
      continue

    index = stats.find('F')
    if (stats[index - 1] == '(') or (index == -1):
      continue
    num = int(stats[index - 1])
    # print(num)

    tokens = stats.split()
    time = tokens[2]

    timeTokens = time.split(':')
    m = 0
    s = 0
    if len(timeTokens) > 1:
      m = int(timeTokens[0])
      s = int(timeTokens[1])
    else:
      s = int(timeTokens[0])

    fixedTime = timedelta(minutes=m, seconds=s).total_seconds()
    # print(fixedTime)

    finalTime = fixedTime/num
    # print(finalTime)
    lastFive.append(finalTime)

    x += 1

  # print(lastFive)
  total = 0;
  factor = 7.99998

  for n in lastFive:
    total+=n

  mean = str(round(total / 5 * factor / 60, 4)).ljust(6,'0')
  mean = mean[:4] + "." + mean[4:]
  print("Mean = "+mean)
  f.write("Mean = "+mean+"\n")

  lastFive.sort()
  median = str(round(lastFive[2] * factor / 60, 4)).ljust(6,'0')
  median = median[:4] + "." + median[4:]

  print("Median = "+median)
  print("===")
  f.write("Median = "+median+"\n")
  f.write("___\n")

f.close()
