

data.loc[data['citric acid'].isnull(), 'citric acid'] = data.groupby('citric acid')['fixed acidity'].transform('mean')
data.loc[data['citric acid'].isnull(), 'citric acid'] = data.groupby('citric acid')['volatile acidity'].transform('mean')
data.loc[data['citric acid'].isnull(), 'citric acid'] = data.groupby('citric acid')['pH'].transform('mean')
data.loc[data['citric acid'].isnull(), 'citric acid'] = data.loc[(data['fixed acidity']>5.2)&(data['fixed acidity']<5.4)]['citric acid'].mean()