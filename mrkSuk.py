import urllib.request as urllib2
from bs4 import BeautifulSoup

snp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

page = urllib2.urlopen(snp500)
soup = BeautifulSoup(page, 'html.parser')

data = {}
table = soup.find('table', attrs={'class':'wikitable'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    d = [ele for ele in cols if ele]
    if d:
        data[d[0]] = d[1:]
print(data['AAPL'])

# you naughty little man