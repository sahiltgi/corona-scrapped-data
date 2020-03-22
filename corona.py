import requests as re
from bs4 import BeautifulSoup

URL = 'https://infographics.channelnewsasia.com/covid-19/map.html'
page = re.get(URL)
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
results = soup.find(id('dataContainer'))
print(results.pr)