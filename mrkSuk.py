import urllib2
from bs4 import BeautifulSoup

snp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

page = urllib2.urlopen(snp500)
soup = BeautifulSoup(page, 'html.parser')