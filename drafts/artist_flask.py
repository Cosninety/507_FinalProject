from artist_database import*
from SI507project_tools import*

#reference project three for flask and database connection

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# print(data_list_1)
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY1'] = 'app security finalprojectpath1287534'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./moma_database.db' # TODO: decide what your new database name will be
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    artists_in = Artist.query.all()
    collection = []
    for i in artists_in:
        collection.append(i.Name)
    # artists_in = "word"
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
    # return render_template('single_image.html')

# http://localhost:5000/art_collection_processed
# @app.route('/processed_images')
# def processed_images():
#     artists_in = Artist.query.all()
#     image_processed = []
#     for i in artists_in:
#         if i not in image_processed:
#             image_processed.append(i.Image_Source) # input processed image
#     return render_template('processed_images.html', image = image_processed )
#     # return render_template('single_image.html')


# http://localhost:5000/add/Noah/Male
@app.route('/add/<name>/<gender>')
def add_artist1(name, gender):
    # return "{} {}".format(name, gender)
    if Artist.query.filter_by(Name=name).first():
        return "That artist already exists! Enter a new/unique artist name"
    else:
        get_or_create_artist(name, gender)

        return "New artist: {} has been added to the repository.".format(name)

# @app.route('/single_image')
# def art_image():
#     one_image = scraped_list_of_lists[0][-1]
#     # print(one_image)
#     return render_template('single_image.html', one_image = one_image )
#     # return render_template('single_image.html')

if __name__ == '__main__':
    # db.create_all()
    # populate_data(scraped_list_of_lists)
    db.init_app(app)
    app.run()
    print('complete 3')
