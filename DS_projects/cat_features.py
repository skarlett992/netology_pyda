# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Handle table-like data and matrices
import numpy as np
import pandas as pd


# Modelling Helpers

from sklearn.preprocessing import LabelEncoder, OneHotEncoder



data = pd.read_csv('winequalityN.csv')



cat_feat_data = data[['type']].apply(LabelEncoder().fit_transform)
num_feat_data = data.drop(['type'], axis=1)
data = pd.concat([num_feat_data, cat_feat_data], axis=1)
cat_feat = cat_feat_data.columns
num_feat = num_feat_data.columns