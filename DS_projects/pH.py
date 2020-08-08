
data.loc[(data['pH'].isnull())&(data['volatile acidity']>=0.2)&(data['volatile acidity']<=0.23), 'pH'] \
= data.groupby('volatile acidity')['pH'].transform('mean')
data.loc[(data['pH'].isnull())&(data['volatile acidity']>=0.28)&(data['volatile acidity']<=0.32), 'pH'] \
= data.groupby('volatile acidity')['pH'].transform('mean')
data.loc[(data['pH'].isnull())&(data['volatile acidity']>=0.43)&(data['volatile acidity']<=0.45), 'pH'] \
= data.groupby('volatile acidity')['pH'].transform('mean')
data.loc[(data['pH'].isnull())&(data['volatile acidity']>=0.695)&(data['volatile acidity']<=0.71), 'pH'] \
= data.groupby('volatile acidity')['pH'].transform('mean')