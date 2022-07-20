import pandas as pd

df = pd.read_csv('main.csv')
del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']

df.to_csv('file.csv')