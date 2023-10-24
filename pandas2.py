import pandas as pd

#read_csv returns a data frame
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
#lets use the head method
print("USING THE HEAD METHOD")
print(data.head(3)) #will print first 3 rows
#tail method
print("USING TAIL METHOD")
print(data.tail(4))

#dataframe has the info methodd which gives details about the data
print("THE INFORMATION IS")
print(df.info())
#THE RESULT TELLS US NUMBER OF ENTRIES(ROWS) and columns, name of each column with data type