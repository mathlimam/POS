import sqlite3 as sql



def conn(db):

    try:
        
        conn = sql.connect(db)
        return conn
    
    
    except Exception as e: 

        print(e)
        return None