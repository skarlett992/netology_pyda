import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('winequalityN.csv')

plt.figure(figsize=(19,2))
sns.boxplot(x=data['alcohol'])
