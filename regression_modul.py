import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from import_data import *
import statsmodels.formula.api as sm

class Regression_Modul:

    
    def __init__(self):

        self.X = X
        self.y = y
        self.X = np.append(arr = np.ones((29,1)).astype(int), values = self.X ,axis=1)
        self.X_opt = self.X[:, [0,1,2,3,4]]
        self.SL = 0.05
        self.X_Modeled = self.backwardElimination(self.X_opt, self.SL)

        #Creating the training set and test set 
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(self.X_Modeled, self.y, test_size = 0.2, random_state = 0)
        
        from sklearn.linear_model import LinearRegression
        self.regressor = LinearRegression()
        self.regressor.fit(X_train, y_train)
        
    #Creating the modul using backwards elemination technique to get only the variables that are needed
    
    def backwardElimination(self,x, sl):
        numVars = len(x[0])
        for i in range(0, numVars):
            regressor_OLS = sm.OLS(self.y, x).fit()
            maxVar = max(regressor_OLS.pvalues).astype(float)
            if maxVar > sl:
                for j in range(0, numVars - i):
                    if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                        x = np.delete(x, j, 1)
        regressor_OLS.summary()
        return x

    #Predicting the result 
    def prediction(self,array):
        #Predicting the results of Test set 
        y_pred = self.regressor.predict(array)
        return y_pred
    
