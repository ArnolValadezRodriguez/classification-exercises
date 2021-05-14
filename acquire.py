from env import host, password, user
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from env import host, user, password
from pydataset import data

# 1. Make a function named get_titanic_data that returns the titanic data from the codeup data science 
# database as a pandas data frame. Obtain your data from the Codeup Data Science Database.

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_titanic_data():
    '''
    This function reads in the titanic data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_connection('titanic_db'))

def get_titanic_data(cached=False):
    '''
    This function reads in titanic data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in titanic df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('titanic_df.csv') == False:
        # Read fresh data from db into a DataFrame.
        df = new_titanic_data()
        # Write DataFrame to a csv file.
        df.to_csv('titanic_df.csv')    
    else:    
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('titanic_df.csv', index_col=0)        
    return df

# 2. Make a function named get_iris_data that returns the data from the iris_db on the codeup data 
# science database as a pandas data frame. The returned data frame should include the actual name of the 
# species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

def new_iris_data():
    '''
    This function reads the iris data from the Codeup db into a df.
    '''
    sql_query = """
                SELECT *
                FROM measurements
                JOIN species USING(species_id)
                """
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    return df

def get_iris_data(cached=False):
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('iris_df.csv'):
        df = pd.read_csv('iris_df.csv', index_col=0)     
    else:
        df = new_iris_data()
        df.to_csv('iris_df.csv')        
    return df

# 3. Once you've got your get_titanic_data and get_iris_data functions written, now it's time to add 
# caching to them. To do this, edit the beginning of the function to check for a local filename like 
# titanic.csv or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the 
# SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the 
# appropriate name.

