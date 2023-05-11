import pandas as pd


#create a dictionary
mydataset={
    'cars':["BMW","Volvo","Ford"],
    'passings':[3,7,2]
}

#convert the dictionary into a data frame
myvar=pd.DataFrame(mydataset)

print(type(myvar))
print(myvar)


#lets create a series
#series is like a column in the table which can hold any data type.
#if nothing else is specified values are labeled with index number
a=[1,7,5]
myvar=pd.Series(a)
print(myvar)
#accesing a series element
print(myvar[2])

#lets create custom indices
myvar=pd.Series(a,index=["x","y","z"])
print(myvar)
print(myvar["z"])
print(myvar[2])

#dictionary as a series
dict_var={
    "day1":23,
    "day2":54,
    "day3":72
}
myvar=pd.Series(dict_var)
print(myvar)
#to include specific indices 
myvar=pd.Series(dict_var,index=["day1","day2"])
print(myvar)


#dictionary as a dataframe
dict_var2={
    "column1":["anirudh","ravi","avinash"],
    "column2":[25,24,23]
}
myvar=pd.DataFrame(dict_var2)
print(myvar)