from urllib.request import urlopen,HTTPError
from bs4 import BeautifulSoup
try:
    html=urlopen("http://www.pythonscraping.com/pages/error.html")
except HTTPError as e:
    print(e)
else:
    bsobj=BeautifulSoup(html.read(), "html.parser")
    print(bsobj.h1)