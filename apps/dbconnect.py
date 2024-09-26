import psycopg2
import pandas as pd 

def getdblocation():
    db = psycopg2.connect(
        host = 'localhost',
        database = 'LARA-database',
        user = 'postgres',
        port = 5432,
        password = 'nat31602'
    )
    return db

def modifydatabase(sql, values):
    db = getdblocation()
    cursor = db.cursor()
    cursor.execute(sql, values)
    db.commit()
    db.close()

def querydatafromdatabase(sql, values, dfcolumns):
    db = getdblocation()
    cursor = db.cursor()
    cursor.execute(sql, values)
    rows = pd.DataFrame(cursor.fetchall(), columns = dfcolumns)
    db.close()
    return rows