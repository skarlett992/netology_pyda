import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('winequalityN.csv')

def plot_distribution( df , var , target , **kwargs ):
    row = kwargs.get( 'row' , None )
    col = kwargs.get( 'col' , None )
    facet = sns.FacetGrid( df , hue=target , aspect=4 , row = row , col = col )
    facet.map( sns.kdeplot , var , shade= True )
    facet.set( xlim=( 0 , df[ var ].max() ) )
    facet.add_legend()

plot_distribution( data , var = 'alcohol' , target = 'quality' , row = 'type' )