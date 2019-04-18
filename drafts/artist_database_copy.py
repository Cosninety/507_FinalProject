from SI507project_tools import*
from artist_flask import*
#
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship


db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy ??Where is this called??? session add and session commit


# see hw5 for ChocolateBars database reference. appending json data to database
#Project 3 for adding to Model database!!!!!!!!
#to prevent duplicate additions Also check out the get_or_create_artist example in the Songs application example we saw, and the additional example in the Populating a database sample in Canvas > Pages > Additional Useful Resources -- you may find that useful. The get_or_create function idea will likely have exactly the effect you want.

class Artist(db.Model):
    __tablename__ = 'artist_Info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    artist_Info = relationship('Artist') # table name = class name

# init_db() how to initiate??
#
def get_or_create_artist(artist_name):
    artist = Arist.query.filter_by(Name=artist_name).first()
    if artist:
        return artist
    else:
        artist = Artist(Name=artist_name)
        session.add(artist)
        session.commit()
        return director

##########
data_list_1 = []
tracker = []
for i in scraped_list_of_lists:
    try:
        data_list_1.append(Artist(Nationality=i[1],Gender=i[2],Name=i[4], Description=i[6], Image_Source=i[7] ))
        # data_list_1.append(Artist(Nationality=i[1],Gender=i[2], Name = i[4]) )
        tracker.append(i)
    except:
        continue
#
for item in data_list_1:
    session.add(item)
    session.commit()
#
# print(data_list_1)

data_list_2 = []

for j in scraped_list_of_lists:
    try:
        if j in tracker:
            data_list_2.append(Classification(Art_type = j[3] ) )
    except:
        continue

for k in data_list_2:
    session.add(k)
    session.commit()

print('complete')
# print(data_list_2)




# #
# @app.route('/')
# def index():
#     # return 'test2'
#     # return render_template('index.html')
#     movies_in = Movie.query.all()
#     num_movies = len(movies_in)
#     return render_template('index.html', num_movies = num_movies)
#0
# @app.route('/add/<name>/<gender>/<description>') ### Add distributor
# def new_song(title, director, genre):
#     if Artist.query.filter_by(name=name).first(): # if there is a movie by that title
#         return "That movie already exists! Go back to the main app!"
#     else:
#         director = get_or_create_artist(director)
#         movie = Movie(title=title, director_id= director.id, genre=genre) # director, not directors.. Activates the return statement in the Movie class
#         session.add(movie)
#         session.commit()
#         return "New movie: {} by {}. Type the URL all_movies to see the whole list of movie in repo.".format(movie.title, director.name)


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    # app.run()
