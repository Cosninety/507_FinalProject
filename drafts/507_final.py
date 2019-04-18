# -*- coding: utf-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

import os #what is this?
import csv
import json
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
import requests, json

from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache

from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security cryptic1276491364'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./nationapark.db' # TODO: decide what your new database name will be
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

#SEE PROJECT 3 AND HW 5 FOR MORE REFERENCE

#Code from sample_scraping_caching.py
FILE_NAME = "moma_collection.json"
PROGRAM_CACHE = Cache(FILE_NAME)
# START_URL = "https://www.moma.org/artists"
START_URL =  "https://www.moma.org/artists/36?locale=en"

#CITATION NEEDED FOR CACHING
def access_page_data(url):
    data = PROGRAM_CACHE.get(url) # instance of Cache(FILE_NAME)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data, expire_in_days=1) #, expire_in_days=1
    return data

artists_page = access_page_data(START_URL)
main_soup = BeautifulSoup(artists_page, "html.parser") #get page


list_items =  main_soup.find('div', class_ = 'primary-sources') #how to check if it exists? attempt the try except pattern...
# print(list_items)
blurb = list_items.find_all('dd', class_ ="text center balance-text")
for i in blurb:
    print(i.get_text().strip())


# pages = [] # gotta get all the data in BeautifulSoup objects to work with...
# for l in all_links :
#     raw_page_data = access_page_data("https://www.nps.gov" + l['href'])
#     clean_page_data = BeautifulSoup(raw_page_data, features = "html.parser")
#     # print(clean_page_data)
#     # list_items =  main_soup.find('ul', class_ = 'link==tile')
#     pages.append(clean_page_data)

# # print(h_search)
# # print(clean_page_data2)
#
# list_of_lists = []
#
# for item in pages:
#     # print(item.title.text)
#     list = []
#
#     parks = item.find_all('ul', id='list_parks')
#
#     for item_2 in parks : # Name of Site
#         type_of_site = item_2.find("h3").get_text()
#         list.append(type_of_site)
#
#     for item_2 in parks : # Type of Site
#         type_of_site = item_2.find("h2").get_text()
#         list.append(type_of_site)
#
#     for item_3 in parks : # Description
#         para = item_2.find("p").get_text()
#         if len(para) > 2:
#             list.append( item_2.find("p").get_text()  )
#         else:
#             list.append("NA")
#
#     for item_4 in parks: # Location
#         location_1 = item_2.find("h4").get_text()
#         list.append(location_1)
#
#     list_of_lists.append(list)
#
# # print(list_of_lists)
#
#
#
#
# with open('national_park.csv', mode = 'w', encoding = 'utf-8' , newline='') as csvfile:
#     park_writer = csv.writer(csvfile)
#     header = "Name , Site Type, Description, Location\n"
#     # header = "Name", "Site Type", "Description", "Location"
#     csvfile.write(header)
#     park_writer.writerows(list_of_lists)
#     # park_writer.writerow(['one','two','three'])

# print(pages)
# print(pages[0].prettify())
