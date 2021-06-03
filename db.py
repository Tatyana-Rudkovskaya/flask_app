import sqlite3
from flask import g
DATABASE = 'database_file.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def add_data(id,username1):  
  try:
    # Connecting to database
    con = sqlite3.connect(DATABASE)
    # Getting cursor
    c =  con.cursor()
    # Adding data
    c.execute("INSERT INTO users VALUES('%s', '%s')" %(id, username1))
    # Applying changes
    con.commit() 
  except ValueError:
    print(ValueError)
    print("An error has occured")