from SI507project_tools import*
from artist_flask import*
#
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY1'] = 'app security finalprojectpath1287534'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./moma_database.db' # TODO: decide what your new database name will be
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
# from db import session , init_db

db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy ??Where is this called??? session add and session commit


# see hw5 for ChocolateBars database reference. appending json data to database
#Project 3 for adding to Model database!!!!!!!!
#to prevent duplicate additions (see project3) Also check out the get_or_create_artist example in the Songs application example we saw, and the additional example in the Populating a database sample in Canvas > Pages > Additional Useful Resources -- you may find that useful. The get_or_create function idea will likely have exactly the effect you want.
# See this for flask and sql alchemy https://github.com/si507-w19/Songs-App-Class-Example/blob/master/main_app.py
#https://umich.instructure.com/courses/269178/pages/additional-useful-resources - TEST SQL OUTPUT !!!!

class Classification(db.Model):
    __tablename__ = 'classification'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Art_type = db.Column(db.String(250))

class Artist(db.Model):
    __tablename__ = 'artist_Info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Catalog_Num =  db.Column(db.Integer)
    Name = db.Column(db.String(250))
    Gender = db.Column(db.String(250))
    Description = db.Column(db.String(250)) #
    Image_Source = db.Column(db.String(250))
    Nationality =  db.Column(db.String(250))
    Classification_Key = db.Column(db.Integer, db.ForeignKey('classification.id')) # table name
    classification = relationship("Classification") # table name = class name


def populate_data(input):
    data_list_2 = []
    tracker = []
    for j in input:
        try:
            type = Classification.query.filter_by(Art_type = j[3]).first() #does artist exist already?
        except:
            continue
        if type:
            return type
        else:
            try:
                data_list_2.append(Classification(Art_type = j[3])  )
                tracker.append(i)
            except:
                continue
    for k in data_list_2:
        session.add(k)
        session.commit()

    data_list_1 = [] # what is this??
    for i in input:
        try:
            artist = Artist.query.filter_by(Name=i[4]).first() #does artist exist already?
        except:
            continue
        if artist:
            return artist
        else:
            try:

                data_list_1.append(Artist(Catalog_Num = i[0], Nationality=i[1],Gender=i[2],Name=i[4], Description=i[6], Image_Source=i[7], Classification_Key = session.query(Classification.id).filter(Classification.Art_type.like(i[3]))#how to
                ))
            except:
                continue
        for item in data_list_1:
            session.add(item)
            session.commit()


    print('complete afterd')

def get_or_create_artist(name, gender):

    artist = Artist(Name=name, Gender=gender)
    session.add(artist)
    session.commit()
    return artist


db.create_all()
populate_data(scraped_list_of_lists)
