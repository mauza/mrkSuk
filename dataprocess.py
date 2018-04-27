import requests
from bs4 import BeautifulSoup

wiki500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(cik)+"&type=10-Q&dateb="+str(priorto)+"&owner=exclude&output=xml&count="+str(count)

r = requests.get(wiki500)

#