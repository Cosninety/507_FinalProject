# Project Title

Noah Garcia - Scraping Data from the Museum of Modern Art collection



https://github.com/Cosninety/507_FinalProject

---

## Project Description

This project scrapes and caches data from MoMa's website and saves the data into a database. The database contains 2 tables with a Many-to-One relationship. A flask web application is initiated in the process. The web application allows users to navigate to different routes, to see images of the artwork, to filter through types of artists and to add names to the database.

## How to run
Note: I am using a Windows system, instruction may vary for Mac OS

1. First, you should run `pip install -r requirements.txt` in the console after initiating a virtual environment.
2. Second, you should run `python artist_flask.py runserver` in the console(scrapes and caches website, creates database, csv file and initiates a local server)
3. Go to a web browser and you should be able to view the index page of my project at http://localhost:5000/

## How to use

1. Once you are in the active index browser a popup alert will trigger saying "This is a Javascript Alert for Noah's project to confirm it's working!!!!" Click okay to close the alert.
2. From the index page a user may click to one between 2 links to see samples images of the artist's work or to filter/search the database to based on type of art.
3. When entering a search keyword in the search route, be sure to enter one of the listed options (Sculptor, Painter, Architect, Photographer)
4. To add an artist to the database, click enter a route following the following syntax(see route 2). The name will appear at the bottom of the list on the index page : /add/name/gender

## Routes in this application

-Route 0: / →  The index page contains links to other routes and a list of all the artist in the database.

-Route 1: /art_collection →   This page will show an images of the artwork in the database

-Route 2: /add/name/gender → This page will add an artist’s name to a list. If the user views the list of artists in the index page, the name will be added to the end of the list.  The route is intended to be a way for people to keep track of which artist’s work they’ve seen.

-Route 3: /search   → This page contains a form. A user may type in one of the following types of artists types to return a list of that type of : Sculptor, Painter, Architect, Photographer

-Route 4: /searchreturn  → After typing in a keyword term in Route 3, this page will load with a list of artists of type searched.

-Route 5: /all_types → Returns list of all artists and what type of artist they are.

## How to run tests
1. run`python SI507project_tests.py` in the console.


## In this repository:
- This README_template.md
- SI507project_tools.py
- SI507project_tests.py
- advanced_expiry_caching.py
- artist_database.py
- artist_flask.py (FILE TO RUN)
- artist_flask.csvfile
- moma_collection.json
- moma_database.db
- SAMPLE_moma_database.db
- requirements.txt (pip INSTALL)
-images
    - databaseSketch_image.jpg
    - Database_Screenshot_1
    - Database_Screenshot_2
    -WebScreenShots and VIDEO demonstration
        - < +/- 7 screenshots of routes >
- templates
    -all_types
    -art_collection
    -index
    -searchreturn
    -searchtype
- static
  -index.js
  -styles.css
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ x ] Project is submitted as a Github repository
- [ x ] Project includes a working Flask application that runs locally on a computer
- [ x ] Project includes at least 1 test suite file with reasonable tests in it.
- [ x ] Includes a `requirements.txt` file containing all required modules to run program
- [ x ] Includes a clear and readable README.md that follows this template
- [ x ] Includes a sample .sqlite/.db file
- [ x ] Includes a diagram of your database schema
- [ x ] Includes EVERY file needed in order to run the project
- [ x ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ x ] Includes at least 3 different routes
- [ x ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ x ] Interactions with a database that has at least 2 tables
- [ x ] At least 1 relationship between 2 tables in database
- [ x ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required) (I utilized 7 of the below components)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ x ] At least one form in your Flask application
- [ x ] Templating in your Flask application
- [ x (and CSS) ] Inclusion of JavaScript files in the application
- [ x ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ x ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ x (used for unittests) ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ x ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ x ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ x ] I included a summary of my project and how I thought it went **in my Canvas submission**!
