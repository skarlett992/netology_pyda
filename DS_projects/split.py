# Handle table-like data and matrices
import pandas as pd


# Modelling Helpers
from sklearn.model_selection import train_test_split , StratifiedKFold
data = pd.read_csv('wine_qual_EDA.csv')
y = data['quality']
X = data.drop(['quality'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y)
