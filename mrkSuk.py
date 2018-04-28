import urllib.request as urllib2
from bs4 import BeautifulSoup

snp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

page = urllib2.urlopen(snp500)
soup = BeautifulSoup(page, 'html.parser')

cik = '0001090872'
data = {}
dataFile = {}

table = soup.find('table', attrs={'class':'wikitable'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    d = [ele for ele in cols if ele]
    if d:
        data[d[0]] = d[1:]

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
#print(data['AAPL'])


def secFile(cik):
    cikUrl = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='+str(cik)+'&type=&dateb=&owner=exclude&start=0&count=100'
    page = urllib2.urlopen(cikUrl)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', attrs={'class':'tableFile2'})

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        d = [ele for ele in cols if ele]

        if d:
            dataFile[d[0]] = d[1:]

        if len(d) == 5:
            data[d[0]] = {
                "Filings": d[1],
                "Format": d[2],
                "Description": d[3],
                "Filing Date": d[4],
                "File Number": d[5]
            }
    print(dataFile)
secFile(cik)

#def getThoseNaughtyBits(penis)

