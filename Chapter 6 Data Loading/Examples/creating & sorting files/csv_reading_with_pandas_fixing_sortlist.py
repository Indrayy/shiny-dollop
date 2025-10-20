import pandas as pd

df = pd.read_csv(r"G:\Engineering & Design Archives\Computing Engineering\Data Science & Engineering Work\Python Grimoire at work\Data Analyst Concepts\Wes McKinney-Python for Data Analyst\Chapter 6 Data Loading\Examples\ex5.csv",
                 delimiter=",",
                 header=0,
                 )

print(df.head())
