import pandas as pd

print('Для фиксированной кислотности пустых строк ' + str( len( data[ pd.isnull( data['fixed acidity'] ) ] ) ))
print('Для летучей кислотности пустых строк ' + str( len( data[ pd.isnull( data['volatile acidity'] ) ] ) ))
print('Для лимонной кислоты пустых строк ' + str( len( data[ pd.isnull( data['citric acid'] ) ] ) ))
print('Для остаточного сахара пустых строк ' + str( len( data[ pd.isnull( data['residual sugar'] ) ] ) ))
print('Для хлоридов пустых строк ' + str( len( data[ pd.isnull( data['chlorides'] ) ] ) ))
print('Для Ph пустых строк ' + str( len( data[ pd.isnull( data['pH'] ) ] ) ))
print('Для сульфатов пустых строк ' + str( len( data[ pd.isnull( data['sulphates'] ) ] ) ))
print('Всего строк в наборе ' + str( len( data ) ))