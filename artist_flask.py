from artist_database import*
from SI507project_tools import*

import os
from flask import Flask, request, render_template, session, redirect, url_for # tools that will make it easier to build on things
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# print(data_list_1)
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY1'] = 'app security finalprojectpath1287534'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./moma_database.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    artists_in = Artist.query.all()
    collection = []
    for i in artists_in:
        collection.append(i.Name)
    num_artists = len(artists_in)
    return render_template('index.html', num_artists = num_artists, collection = collection)

# http://localhost:5000/art_collection
@app.route('/art_collection')
def art_image():
    artists_in = Artist.query.all()
    image = []
    for i in artists_in:
        if i not in image:
            image.append(i.Image_Source)
    return render_template('art_collection.html', image = image[1:] )

# http://localhost:5000/add/Noah/Male
@app.route('/add/<name>/<gender>')
def add_artist1(name, gender):
    # return "{} {}".format(name, gender)
    if Artist.query.filter_by(Name=name).first():
        return "That artist already exists! Enter a new/unique artist name"
    else:
        get_or_create_artist(name, gender)
        return "New artist: {} has been added to the repository.".format(name)

# http://localhost:5000/search
@app.route('/search')
def search():
    return render_template('searchtype.html')

# http://localhost:5000/searchreturn
@app.route('/searchreturn') #Function adapted from Zhen's lecture 26 example #Returns list of artists of a particular type based on form search
def search_type():
    if request.method == 'GET':
        artist_of_type = []
        artists_in = Artist.query.all()
        keyword = request.args.get('keyword')
        no = request.args.get('no')
        keyword = keyword if keyword else 'Artist'
        for i in artists_in:
            type1 = Classification.query.filter_by(id= i.Classification_Key).first()
            try:
                if keyword in type1.Art_type:
                    artist_of_type.append((i.Name, type1.Art_type))
            except:
                continue
        # artist_of_type = Artist.query.filter_by(Classification_Key= keyword)
        return render_template('searchreturn.html', keyword_return = artist_of_type, keyword = keyword )


# # http://localhost:5000/all_types
@app.route('/all_types') #Returns list of all artists and their art style/type
def all_type():
    artist_of_type = []
    artists_in = Artist.query.all()
    for i in artists_in:
        type1 = Classification.query.filter_by(id= i.Classification_Key).first()
        try:
            artist_of_type.append((i.Name, type1.Art_type))
        except:
            continue
    return render_template('all_types.html', keyword_return = artist_of_type)


if __name__ == '__main__':

    db.init_app(app)
    app.run()
    print('complete 3')
