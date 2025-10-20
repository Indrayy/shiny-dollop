import pandas as pd

# Load CSV file

df = pd.read_csv(r"G:\Engineering & Design Archives\Computing Engineering\Data Science & Engineering Work\Python Grimoire at work\Data Analyst Concepts\Wes McKinney-Python for Data Analyst\Chapter 6 Data Loading\Examples\ex5.csv",
                 delimiter=",",
                 names=["something"])

print(df)

# if there is updating, removing, and replacing values.
# Suddenly the result of sort and list also Nan value looks messing,
#you have to use:

#print(df.sort_values(by="something"))  # Sorting by column 'something'

#print(df.columns)
