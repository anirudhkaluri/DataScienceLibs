import pandas as pd

df=pd.read_csv('data.csv')
data=df.to_string()
print(df.head())