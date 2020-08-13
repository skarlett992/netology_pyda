import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('winequalityN.csv')

def plot_correlation_map( data ):
    sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0) 
    fig=plt.gcf()
    fig.set_size_inches(15,10)
    plt.show()
    
plot_correlation_map( data )