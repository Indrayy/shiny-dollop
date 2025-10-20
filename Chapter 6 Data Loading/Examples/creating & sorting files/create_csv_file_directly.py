import csv


data = [
         ["something","a","b","c","d","message"],
	 ["one","1","2","3","4","NA"],
	 ["two","5","6","","8","world"],
	 ["three","9","10","11","12","Foo"]
        ]

# Writing data to CSV

with open(r"G:\Engineering & Design Archives\Computing Engineering\Data Science & Engineering Work\Python Grimoire at work\Data Analyst Concepts\Wes McKinney-Python for Data Analyst\Chapter 6 Data Loading\Examples/ex5.csv", "w", newline="")as f:
	writer = csv.writer(f)
	writer.writerows(data)
	
