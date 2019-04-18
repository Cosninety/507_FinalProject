from SI507project_tools import*



#reference project three for flask and database connection

@app.route('/')
def index():
    # image_path = image_extention
    # return render_template('index.html', artist_image = image_path)
    pass
    # thumbnail = list_items.find('div', class_ ="thumb-image")
    # return(image_extention
    # return requests.get(image_extention)
    # return testimage
    # return testtext


@app.route('/<artist>/img/')
def art_image(artist):
    # image_path = image_extention
    # return render_template('index.html', artist_image = image_path)
    pass

@app.route('/<artist>/blurb/')
def description(artist):
    pass

@app.route('/<artist>/add/')
def add_artist(artist):
    pass


if __name__ == '__main__':
    # db.create_all() #
    app.run()
