#funtion for export to sql

#import dependencies and config
from config import password
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

#set parameters for sql database
params = {"host": "localhost", "user": "postgres", "password": password, "port": 5432}

#create MyDB class
class MyDB(object):
    def __init__(self):
        self.params = params
    
    #create a function to create a new database in sql
    def create_new_db(self, newdb):
        user, host, port = self.params['user'], self.params['host'], self.params['port']
        pw = self.params['password']
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, pw, host, port, newdb)
        
        self.engine = create_engine(url, client_encoding='utf8')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
    
    #create a function to export crime data to sql
    def df1postgres(self, df):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(params['user'], params['password'], params['host'], params['port'], 'test') #name of db
        conn = create_engine(url)
        df.to_sql(name='crime_data', con=conn, if_exists='replace', index=False, chunksize=100)
    
    #create a function to export housing data to sql
    def df2postgres(self, df):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(params['user'], params['password'], params['host'], params['port'], 'test') #name of db
        conn = create_engine(url)
        df.to_sql(name='housing_data', con=conn, if_exists='replace', index=False, chunksize=10)
        
        return conn

db = MyDB()
db.create_new_db('test') #name of db

crime_data = pd.read_csv('Resources/Crime_Reports.csv')
housing_data = pd.read_csv('Resources/austinHousingData.csv')

#dataframe name 1
con1 = db.df1postgres(crime_data)

#dataframe name 2
con2 = db.df2postgres(housing_data) 

#create connection 
conn = psycopg2.connect(dbname='test', user=params['user'], password=password, host=params['host'])

# check if connection to import crime data works
# crime_df = pd.read_sql_query('select * from "crime_data" limit 1',con=conn) 

# check if connection to import housing data works
# housing_df = pd.read_sql_query('select * from "housing_data" limit 1',con=conn) 

#insert sql query to merge crime and housing dataframe before importing to jupyter notebook

#close connection
conn.close()