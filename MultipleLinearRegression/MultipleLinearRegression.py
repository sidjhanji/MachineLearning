# Multiple Linear Regression
# The dataaset include the Marketing spend, R&D Spend, Administration spend, state 
# & the profit for 50 startups. Our Aim is to find investing in which domain could 
# help improve the profit.

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')

# Dividing the dataset into Independent(X) & Dependent(y) variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# to view the complete data in the console for object type
np.set_printoptions(threshold=np.nan)

# State is a categorical variable. Encoding the categorical Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Encoding the independent variable
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
# Label encoder will categories into 0,1,2..
# Computer will think 2>1.. But thats not the case.
# To avoid that we encode into 0/1 values
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap. Do not take all the encoded variables.
# Take one less than the number of categories.
X = X[:, 1:] 

# Splitting the data into training & test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test Results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
