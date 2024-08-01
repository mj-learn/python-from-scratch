import pandas

data = pandas.read_csv("04-Central_Park_Squirrel_Data.csv")
data["Primary Fur Color"].value_counts().to_csv("04-Squirrel-DATA-analysis.csv")
