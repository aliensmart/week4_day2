import sqlite3
import os 

DIR = os.path.dirname(__file__)
DBFILENAME = "tsla.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connect :
        cur = connect.cursor()
        SQL = "DROP TABLE IF EXISTS tsla;"
        cur.execute(SQL)

        SQL = """
            CREATE TABLE tsla(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                Open FLOAT,
                High FLOAT,
                Low FLOAT,
                Close FLOAT,
                Adj_Close FLOAT,
                Volume INTEGER
            );
        """

        cur.execute(SQL)