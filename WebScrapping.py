# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:18:24 20224

@author: anupg
"""
from distutils.filelist import findall
import pip._vendor.requests
from bs4 import BeautifulSoup

print()
no_of_movies=input("How many movie you want to search? ")
print()
url="https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+no_of_movies
req=pip._vendor.requests.get(url)
temp=BeautifulSoup(req.content,"html.parser")
x=temp.find_all("div",class_="lister-item mode-advanced")
for i in x:
    print("Movie Name: "+i.h3.a.text.strip())
    print("Genre: "+i.find("span",class_="genre").text.strip())
    print("Rating: "+i.find("strong").text)
    print('*********************************************')