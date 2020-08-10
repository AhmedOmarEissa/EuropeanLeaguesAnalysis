
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sqlite3 #sql database
import matplotlib.pyplot as plt #plots


conn = sqlite3.connect('database.sqlite') #reading database

def desc():
    '''Show description of database tables'''
    conn = sqlite3.connect('database.sqlite') #reading database
    tables = pd.read_sql("""SELECT *
                            FROM sqlite_master
                            WHERE type='table';""", conn)
    desc  = pd.DataFrame(columns = ['table','rows','columns'])

    for i in tables.name:
        rows  = int(pd.read_sql("""SELECT count(*) FROM """ +i+ """ ;""", conn).values)
        columns = len(pd.read_sql("""select * from """ +i+ """ limit 0 ;""", conn).columns)

        desc = desc.append({'table':i, 'rows':rows , 'columns': columns}, ignore_index=True)

    return desc

def col_of_table(name):
    return list(pd.read_sql("""select * from """ +name+ """ limit 0 ;""", conn).columns)

def head_of_table(name , n=10 ):
    return pd.read_sql("""select * from """ +name+ """ limit """ + str(n) , conn)
