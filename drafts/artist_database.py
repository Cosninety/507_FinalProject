from SI507project_tools import*
from artist_flask import*
#
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

# from db import session , init_db

db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy ??Where is this called??? session add and session commit

# see hw5 for ChocolateBars database reference. appending json data to database
#Project 3 for adding to Model database!!!!!!!!
#to prevent duplicate additions (see project3) Also check out the get_or_create_artist example in the Songs application example we saw, and the additional example in the Populating a database sample in Canvas > Pages > Additional Useful Resources -- you may find that useful. The get_or_create function idea will likely have exactly the effect you want.
# See this for flask and sql alchemy https://github.com/si507-w19/Songs-App-Class-Example/blob/master/main_app.py
#https://umich.instructure.com/courses/269178/pages/additional-useful-resources - TEST SQL OUTPUT !!!!

class Artist(db.Model):
    __tablename__ = 'artist_Info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Catalog_Num =  db.Column(db.Integer)
    Name = db.Column(db.String(250))
    Gender = db.Column(db.String(250))
    Description = db.Column(db.String(250)) #
    Image_Source = db.Column(db.String(250))
    Nationality =  db.Column(db.String(250))

class Classification(db.Model):
    __tablename__ = 'classification'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Art_type = db.Column(db.String(250))
    ##see hw 5 for foreign key relationship
    Artist_Key = db.Column(db.Integer, db.ForeignKey('artist_Info.id')) # table name
    artist_Info = relationship("Artist") # table name = class name

def populate_data(input):
    # input = input
    data_list_1 = []
    tracker = []
    for i in input:
        try:
            artist = Artist.query.filter_by(Name=i[4]).first() #does artist exist already?
        except:
            continue

        if artist:
            return artist
        else:
            try:
                data_list_1.append(Artist(Catalog_Num = i[0], Nationality=i[1],Gender=i[2],Name=i[4], Description=i[6], Image_Source=i[7] ))
        # data_list_1.append(Artist(Nationality=i[1],Gender=i[2], Name = i[4]) )
                tracker.append(i)
            except:
                continue

        for item in data_list_1:
            session.add(item)
            session.commit()

    data_list_2 = []
    # for j in scraped_list_of_lists:
    for j in input:
        try:
            data_list_2.append(Classification(Art_type = j[3]   ) )

# Artist_Key = session.query(Artist.id).filter(Artist.Name.like(j['Catalog_Num']))
            # print(Classification(Art_type = j[3] ))
        except:
            continue
        for k in data_list_2:
            session.add(k)
            session.commit()

print('complete 1')

# populate_data(scraped_list_of_lists)

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    populate_data(scraped_list_of_lists)
    print('complete 2')

    # populate_data({Nationality='American',Gender='Trans', Art_type ='Sculptor', Name='Herma'})

    # app.run()
