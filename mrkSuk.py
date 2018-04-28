import urllib.request as urllib2
from bs4 import BeautifulSoup
import re

snp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sec_base = 'https://www.sec.gov/'

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
    buttons = soup.find_all('a', {'id': 'documentsbutton'})

    page_urls = []
    for a in buttons:
        page_urls.append(a.attrs['href'])
    
    file_urls = []
    for u in page_urls:
        url = sec_base + u
        doc_page = urllib2.urlopen(url)
        soup2 = BeautifulSoup(doc_page, 'html.parser')
        file_name = soup2.find(text=re.compile('.*\.htm$'))
        if file_name:
            file_urls.append(file_name.parent.attrs['href'])
    print(len(file_urls))


secFile(cik)

#def getThoseNaughtyBits(penis)

