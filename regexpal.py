from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj=BeautifulSoup(html,"html.parser")
images=bsobj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
#myTag.attrs
#myImagTag.attrs['src']
a=bsobj.findAll(lambda tag:len(tag.attrs)==2)
for a1 in a:
    print(a1)
#for images in images:
#    print(images["src"])