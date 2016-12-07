from bs4 import BeautifulSoup
import requests
import re

url = "https://scholar.google.pl/citations?view_op=view_org&hl=pl&org=13284653006361851988"
r = requests.get(url)

astart = 10
for i in range(0,10):
    try:
        #nxt = url.format(start)
        #r = requests.get(nxt)
        soup = BeautifulSoup(r.content, "html.parser")
        print(soup.find("h3", {"class": "gsc_1usr_name"}))
        buttonString = soup.find("button",{"class":"gs_btnPR gs_in_ib gs_btn_half gs_btn_srt"})
        str1 = str(buttonString)
        after_author = re.split("x3d*",str1)
        after_author = after_author[5][0:12]
        start = str(astart)
        payload = {'after_author': after_author, 'astart': start}
        r = requests.get(url, params=payload)
    except Exception as e:
        print(e)
        break
    astart += 10
