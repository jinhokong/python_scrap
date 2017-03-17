from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def gettitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj=BeautifulSoup(html.read(), "html.parser")
        title=bsobj.body.h1
    except AttributeError as e:
        return None
    return title
title=gettitle("http://www.pythonscraping.com/pages/page1.html")
if title== None:
    print("title could not found.")
else:
    print(title)