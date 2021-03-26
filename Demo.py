import requests as req
from bs4 import BeautifulSoup
r=req.get(
    "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
r.encoding= "utf8"
if r.status_code==200:
    #print(r.text)
    soup=BeautifulSoup(r.text,"lxml")
    #print(soup)
    result1=soup.find_all("p")
    fp=open("out2.txt","w",encoding="utf8")
    #print(result1)
    for val in result1:
        #print(val.text)
        text2=val.text.replace('\n','')
        #print(text2)
        text3=text2.replace('  ','')
        print(text3)
        fp.write(text3+'\n')
    fp.close()
else:
    print("no page")