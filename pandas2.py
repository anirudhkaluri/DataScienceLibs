import pandas as pd

df=pd.read_csv('data.csv')
#print first few rows
print(df.head())

#lets see how many maxiumum rows by default pandas displays
print(pd.options.display.max_rows)
#lets change it
pd.options.display.max_rows=98

#lets try to read json file
data=pd.read_json('data.json')
df=pd.DataFrame(data)
print(df)
