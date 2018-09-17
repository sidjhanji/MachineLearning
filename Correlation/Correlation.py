#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:22:49 2018

@author: sjhanji
"""

# Understanding correlation & Feature selection.
# Dataset: Breast Cancer Wisconsin (Diagnostic) Data Set

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading from the dataset
dataset = pd.read_csv('data.csv')
dataset.head()
dataset.info()

# Removing the two columns
dataset = dataset.iloc[:, 1:-1]
dataset.info()

# Encoding the dignosis variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder = LabelEncoder()
dataset.iloc[:,0] = labelEncoder.fit_transform(dataset.iloc[:,0]).astype('float64')

dataset.info()

dataset.describe()

# Find the correlation between the variables
corr = dataset.corr()
corr.head()



# Seaborn for plotting corr heatmap
import seaborn as sns
sns.heatmap(corr)

# Compare the correlation between features and remove one of the two features 
# that have a correlation higher than 0.9
columns = np.full((corr.shape[0]), True, dtype=bool)
columns
corr.shape[0]

for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False

selectedColumns = dataset.columns[columns]
selectedColumns.shape

dataset = dataset[selectedColumns]

# Remove the dignosis column as it is what we have to predit
selectedColumns = selectedColumns[1:].values
selectedColumns.shape

# Check the values to be usede in the function creation
x = dataset.iloc[:, 1:].values
len(x[0])

# Function for Backward Elimination
import statsmodel.formula.api as sm
def backwardElimination(x, Y, sl, columns):
    numVars =  len(x[0])
    for i in range(0, numVars):
        

