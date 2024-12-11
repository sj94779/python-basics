import pandas as pd

mydataset = {
    "cars" : ["BMW", "Audi", "Tesla"],
    "passings": [1,4,7]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

a = [1,7,2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

myvar = pd.Series(a , index=["x", "y" ,"z"])
print(myvar)
print(myvar["y"])

#Series is like a column, a DataFrame is the whole table.

calories = {"day1":420, "day2":450, "day3":300}
myvar = pd.Series(calories)
print(myvar)

myvar = pd.Series(calories, index= ["day1", "day3"])
print(myvar)

data = {
    "calories":[420,450,300],
    "duration":[40,50,20]
}

myvar = pd.DataFrame(data)

print(myvar)
#to get row 1
print(myvar.loc[0])

myvar = pd.DataFrame(data, index=["x","y","z"])
print(myvar)
print(myvar.loc["x"])

#read csv

df = pd.read_csv('data.csv')
print(df.to_string())


print("only first and last 5")
print(df)

print(pd.options.display.max_rows)
# 169>60 so print(df) will return header first 5 and last 5 only

#we can increase max row
pd.options.display.max_rows = 9999


df = pd.read_json("data.json")
print(df.to_string())

print("only 10 values")
df = pd.read_csv("data.csv")
print(df.head(10))

print("only first 5")
print(df.head())
print("only last 5")
print(df.tail())


#info
print(df.info())
