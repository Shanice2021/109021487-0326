import requests as req
from bs4 import BeautifulSoup
r=req.get(
    "http://120.108.116.237/~jackjow/pubList.php")
r.encoding= "utf8"
if r.status_code==200:
#    print(r.text)
    soup=BeautifulSoup(r.text,"lxml")
#    print(soup)
    result1=soup.find_all("li")
    print(result1)
else:
    print("no page")