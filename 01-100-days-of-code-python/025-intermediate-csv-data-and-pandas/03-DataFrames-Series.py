# DataFrame: A two-dimensional, labeled data structure with rows and columns.
# Series: A one-dimensional labeled array, similar to a column in a DataFrame.
# Rows: Horizontal records in a DataFrame, representing individual observations.
# Columns: Vertical records in a DataFrame, representing different variables.

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

temp_list = data["temp"].to_list()
print(temp_list)

# Calculate the average temperature
average_temp = sum(temp_list) / len(temp_list)

print(average_temp)
print(data["temp"].mean())

# Max temperature
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)
