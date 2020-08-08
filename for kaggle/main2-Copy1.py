import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from catboost import CatBoostClassifier


def get_features_from_df(frame):
    f = pd.concat([frame['surname'].str[0].str.isupper().rename('first_upper')] +
                  [(frame['surname'].str[0].str.isupper() & frame['surname'].str[1:].str.islower()).rename('only_first_upper')] +
                  [frame['surname'].str.isupper().rename('all_upper')] +
                  [frame['surname'].str.lower().str[i].rename(i) for i in range(-last_n, 0)], axis=1)
    return f


df = pd.read_csv('linear_train.txt', header=None).iloc[:20000000].rename(columns={0: 'surname', 1: 'target'})
df = df.append(pd.read_csv('linear_test.txt', header=None).iloc[:2000000].rename(columns={0: 'surname', 1: 'target'}), ignore_index=True, sort=False)

last_n = 4

y = df['target']
x = get_features_from_df(df)

x = pd.get_dummies(x, columns=range(-last_n, 0))

x, x_final, y, y_final = x[pd.notnull(y)], x[pd.isnull(y)], y[pd.notnull(y)], y[pd.isnull(y)]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

clf = CatBoostClassifier(n_estimators=300, learning_rate=0.2, max_depth=6, eval_metric='AUC')
clf.fit(x_train, y_train, eval_set=[(x_train, y_train), (x_test, y_test)])
y_pred_train, y_pred_test = clf.predict_proba(x_train)[:, 1], clf.predict_proba(x_test)[:, 1]
print(f'{roc_auc_score(y_train, y_pred_train):.3f}, {roc_auc_score(y_test, y_pred_test):.3f}')

#result = pd.concat([pd.Series(df2.index, name='Id'), pd.Series(y2, name='Answer')], axis=1)
#result.to_csv('result.txt', index=False)

