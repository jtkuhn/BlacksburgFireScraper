import sqlite3

databaseFile = "output/db.sqlite"

#This database contains a column for each important piece of information per record
#The columns named full_XXX are the exact parsed string for XXX out of the data
databaseCreationString = """ CREATE TABLE IF NOT EXISTS records (
        id TEXT PRIMARY KEY,
        dispatchDateTime TEXT,
        full_dispatchDateTime TEXT,
        location TEXT,
        full_location TEXT,
        type TEXT,
        full_type TEXT
    ); """


def createDatabase():
    conn = sqlite3.connect(databaseFile)
    c = conn.cursor()
    
    c.execute(databaseCreationString)
    
    conn.close()


if __name__ == "__main__":
    print("Don't run this! Import it to use elsewhere.")