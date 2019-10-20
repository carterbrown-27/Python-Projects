import json
import requests

year = input("Enter the year for the standings, with 2018-2019 szn as 2018: ")
szn = year + str(int(year)+1)

headers = {
  'Referer': 'https://www.nhl.com/standings/'+str(year)+'/league'
}

params = (
  ('hydrate', 'record(overall),division,conference,team'),
  ('season', szn),
)

response = requests.get('https://statsapi.web.nhl.com/api/v1/standings', headers=headers, params=params)
# print(response.content)

# get standings (in the 4 divisions)
JSON = json.loads(response.content)
records = JSON['records']

teams = []
teamsChecked = 0
for division in records:
  standings = division['teamRecords']
  #print(standings)
  for team in standings:
    teamMeta = team['team']
    # print(team)
    # out = teamMeta['name']+": "+str(team['points'])
    # print(out)
    teams.append([teamMeta['name'],team['points']])
    teamsChecked += 1

def getPts(i):
  return i[1]
teams.sort(reverse=True, key=getPts)

for team in teams:
  print(team[0] + ": " + str(team[1]))
print(teamsChecked)
