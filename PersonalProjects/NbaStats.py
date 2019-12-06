from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#Year of stats to be scraped
year = 2019

#Page to be scraped
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

#HTML from given url
html = urlopen(url)

soup = BeautifulSoup(html, features='lxml')

#Getting column headers
soup.findAll('tr', limit=2)

#Use getText() to extract all text
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

#Excludes first column
headers = headers[1:]


#Avoid first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
    for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns=headers)
stats.head(10)

print(stats)


