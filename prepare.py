# The end product of this exercise should be the specified functions in a python script named prepare.py. 
# Do these in your classification_exercises.ipynb first, then transfer to the prepare.py file.

from env import host, password, user
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from env import host, user, password
from pydataset import data

def prep_iris(df):
    '''
    takes in a dataframe of the iris dataset as it is acquired and returns a cleaned dataframe
    arguments: df: a pandas DataFrame with the expected feature names and columns
    return: clean_df: a dataframe with the cleaning operations performed on it
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['species_id', 'measurement_id'])
    df = df.rename(columns= {'species_name':'species'})
    dummy_iris_df = pd.get_dummies(df[['species',]], dummy_na=False, drop_first=[True])
    df = pd.concat([df, dummy_iris_df], axis=1)
    return df.drop(columns=['species'])