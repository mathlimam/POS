import sqlite3 as sql



def conn(database):

    try:
        
        conn = sql.connect(database)
        return conn
    
    
    except Exception as e: 
        return e