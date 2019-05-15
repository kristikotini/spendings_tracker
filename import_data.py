import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename='Spendings.csv'
#Importing the data


dataset = pd.read_csv(filename)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
    
def get_clothes_data():
    return X[:,1]
def get_food_data():
    return X[:,2]
def get_free_time_data():
    return X[:,3]
def get_spendings():
    return X[:,-1]
def get_savings():
    savings=0
    for i in y:
        savings+=i
    return savings

        
          
