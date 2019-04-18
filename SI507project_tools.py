# -*- coding: utf-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

import os #what is this?
import csv
import json
import requests, json

from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security cryptic12uyv76491364'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./moma_database.db' # TODO: decide what your new database name will be
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache

#SEE PROJECT 3 AND HW 5 FOR MORE REFERENCE

#Code from sample_scraping_caching.py # Citation needed
FILE_NAME = "moma_collection.json"
PROGRAM_CACHE = Cache(FILE_NAME)
START_URL = "https://www.moma.org/artists"
# START_URL =  "https://www.moma.org/artists/39?locale=en"

#CITATION NEEDED FOR CACHING
def access_page_data(url):
    data = PROGRAM_CACHE.get(url) # instance of Cache(FILE_NAME)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data, expire_in_days= 14) #, expire_in_days=1

    return data


artists_page = access_page_data(START_URL)

print(type(artists_page))

main_soup = BeautifulSoup(artists_page, "html.parser") #get page
# print(main_soup)

# list_items =  main_soup.find('div', class_ ='tile-container')
list_items =  main_soup.find('div', class_ ='flex')
all_links = list_items.find_all('a')

pages = [] # gotta get all the data in BeautifulSoup objects to work with...
for l in all_links :
    raw_page_data = access_page_data("https://www.moma.org" + l['href'])
    clean_page_data = BeautifulSoup(raw_page_data, features = "html.parser")
    pages.append(clean_page_data)

# print(pages)

scraped_list_of_lists = []
# scraped_list_of_lists = []
for item in pages:
    # print(item.title.text)
    list = []
    try:
        list_items =  item.find('div', class_ = 'primary-sources')
        blurb = list_items.find_all('dd', class_ ="text center balance-text")
        for i in blurb:
            list.append(i.get_text().strip())
            # print(i.get_text().strip())

        description = item.find('div', class_ = 'primary-source')
        excerpt = description.find('dd', class_ = 'text center')
        # print(excerpt.text)
        list.append(excerpt.get_text())

        image = item.find('img')
        EXTENTION = "https://www.moma.org" #eero aarnio
        # print(EXTENTION  + image.get('src'))
        image_extention = EXTENTION  + image.get('src')
        if len(image_extention) > 20:
            list.append(image_extention)
        else:
            list.append("No image")
        #append Description to list too !!!
    except:
        continue
        # print("not an artist profile. Search another option")


    scraped_list_of_lists.append(list)

# print(list_of_lists)


with open('artists_spread.csv', mode = 'w', encoding = 'utf-8' , newline='') as csvfile:
    fieldnames = ["Catalog Number","Nationality", "Sex", "Art_type", "Name", "Catalog Number2", "Description", "Image Source"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    for i in scraped_list_of_lists:
        try:
            writer.writerow({'Catalog Number':i[0], "Nationality" :i[1] ,"Sex" :i[2],"Art_type" :i[-5], "Name" :i[-4],"Catalog Number2" :i[-3], "Description": i[-2] , "Image Source": i[-1] })
        except:
            continue
