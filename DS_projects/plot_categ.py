import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('winequalityN.csv')

def plot_categories( df , cat , target , **kwargs ):
    row = kwargs.get( 'row' , None )
    col = kwargs.get( 'col' , None )
    facet = sns.FacetGrid( df , row = row , col = col )
    facet.map( sns.barplot , cat , target )
    facet.add_legend()

plot_categories( data , cat = 'type' , target = 'quality' )