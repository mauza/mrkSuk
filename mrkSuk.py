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
    if len(d) == 8:
        data[d[0]] = {
            "Company Name": d[1],
            "CIK": d[7],
            "Sector": d[3],
            "Sub Industry": d[4],
            "Headquarters": d[5],
            "Start Date": d[6]
        }
    elif len(d) == 7:
        data[d[0]] = {
            "Company Name": d[1],
            "CIK": d[6],
            "Sector": d[3],
            "Sub Industry": d[4],
            "Headquarters": d[5]
        }
print(data['AAPL'])

cik = data['AAPL']["CIK"]
print(cik)
# you naughty little man