import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'resultsTable'})

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print cell.text.replace('&nbsp;', '')