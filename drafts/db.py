#boiler plate base from class resources
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

Base = declarative_base() # Set up base

session = scoped_session(sessionmaker()) # The scoped_session() function is provided which produces a thread-managed registry of Session objects.
# It is commonly used in web applications so that a single global variable can be used to safely represent transactional sessions with sets of objects, localized to a single thread.
# Similar to session = DBSession(), which is described below, but safer (safe ~= no errors) for some types of complex processes.

# A DBSession() instance establishes all conversations with the database and represents a "staging zone" for all the objects loaded into the database session object, like our overall Python programs did before.  Now it's managed more 'centrally' in one instance of an object.
# Any change made against the objects in the session won't be persisted into the database until you call session.commit(). Handling all the connnection-commit stuff you saw with the raw code.
# If you're not happy about the changes, you can revert all of them back to the last commit by calling session.rollback() -- in the same script... as long as you're still in the same 'session'!
# DBSession = sessionmaker()
# session = DBSession() # Not using these -- as shown in reading -- because of use of the above sessionmaker()


# Now, create an engine that stores data in the local directory's sqlalchemy_example.db/sqlite file.
engine = create_engine('sqlite:///artist_database.sqlite', echo=False) # You might also have a config file, for example, that holds the string that is the db name. For now we'll just put it here.

# Now, bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
session.configure(bind=engine)

def init_db():
    # Drop all tables in the engine if needed for initialization. This is equivalent to "Delete Table" statements in raw SQL.
    # We'll leave this commented out initially, but if you wanted to drop everything and 'reset' it every time, you might uncomment this.
    # Base.metadata.drop_all(engine)

    # Create all tables in the engine. This is equivalent to "Create Table" //TABLES CREATED
    # statements in raw SQL.
    # But, this won't overwrite existing tables -- it will simply create new ones if necessary.
    Base.metadata.create_all(engine) #TABLES CREATED HERE
    return engine # Returning the engine makes it possible to use this function in other files (e.g. query files) to access the engine and use it
