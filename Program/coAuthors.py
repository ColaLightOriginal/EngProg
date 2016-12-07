# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import sys


url = "https://scholar.google.pl/citations?view_op=view_org&hl=pl&org=13284653006361851988"
r = requests.get(url)
googleUrl = "https://scholar.google.pl"

for i in range(0,1):
    try:
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.find('h3',{'class': "gsc_1usr_name"}):
            #linq = link.a
            #linq = linq.get('href')

            #Go to profile
            url = googleUrl + link.get('href') + '&cstart=0&pagesize=1000'
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")

            #Go to document
            for document in soup.find_all('tr', {'class': 'gsc_a_tr'}):
                link = document.a
                link = link.get('href')
                #encode('utf-8')
                url = googleUrl + link
                r = requests.get(url)
                soup = BeautifulSoup(r.content, "html.parser")
                #Get the coauthors
                authors = soup.find('div', {'class': 'gsc_value'})
                print(authors.text)
            #document = soup.find('a', {'class': 'gsc_a_at'})
            #url = googleUrl + document.get('href')
            #r = requests.get(url)
            #soup = BeautifulSoup(r.content, "html.parser")


            #Get the coauthors
            #authors = soup.find('div', {'class': 'gsc_value'})
            #print(authors.text)

    except Exception as e:
        print(e)
        break
