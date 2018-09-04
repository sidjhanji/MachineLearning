# Simple Linear Regression
# We have a data set of employees with years of experience & Salary.

# Importing the Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset 
dataset = pd.read_csv('Salary_Data.csv')
# Splitting the data into independent & dependent variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Divide the data set into Training & Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fit the linear Regression Model to the training data 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the results for the test set
y_pred = regressor.predict(X_test)

# Visualizing the Training Set Results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary Increase with Experience(Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

# Visualizing the Test Set Results
plt.scatter(X_test, y_test, color = 'red')
# The model is trained on the training set so the regressor line will be based 
# on the training set.
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary Increase with Experience(Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
