
data.loc[data['sulphates'].isnull(), 'sulphates'] = data.groupby('chlorides')['sulphates'].transform('mean')