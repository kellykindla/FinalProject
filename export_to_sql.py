#funtion for export to sql
from config import password
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

params = {"host": "localhost", "user": "postgres", "password": password, "port": 5432}

class MyDB(object):
    def __init__(self):
        self.params = params
        
    def create_new_db(self, newdb):
        user, host, port = self.params['user'], self.params['host'], self.params['port']
        pw = self.params['password']
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, pw, host, port, newdb)
        
        self.engine = create_engine(url, client_encoding='utf8')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            
    def df1postgres(self, df):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(params['user'], params['password'], params['host'], params['port'], 'test1') #name of db1
        conn = create_engine(url)
        df.to_sql(name='dummy_table', con=conn, if_exists='replace', index=False, chunksize=10)
        
    def df2postgres(self, df):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(params['user'], params['password'], params['host'], params['port'], 'test2') #name of db2
        conn = create_engine(url)
        df.to_sql(name='dummy_table', con=conn, if_exists='replace', index=False, chunksize=10)
        
        return conn

# db1 = MyDB()
# db1.create_new_db('test1') #name of db1
# df1 = pd.read_csv('') #location and filename of csv1
# con1 = db1.df1postgres(df1) #dataframe name 1

# db2 = MyDB()
# db2.create_new_db('test2') #name of db2
# df2 = pd.read_csv('') #location and filename of csv2
# con2 = db2.df2postgres(df2) #dataframe name 2

# retreive_data = con.execute("select * from table")
# print(retrieve_data.fetchall())