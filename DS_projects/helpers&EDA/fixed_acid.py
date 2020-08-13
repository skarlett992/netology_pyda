
data.loc[data['fixed acidity'].isnull(), 'fixed acidity'] = data.groupby('density')['fixed acidity'].transform('mean')
data.loc[data['fixed acidity'].isnull(), 'fixed acidity'] = data.loc[(data['density']>0.9963)&(data['density']<0.9964)]['fixed acidity'].mean()
