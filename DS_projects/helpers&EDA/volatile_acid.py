
data.loc[data['volatile acidity'].isnull(), 'volatile acidity'] = data.groupby('chlorides')['volatile acidity'].transform('mean')
