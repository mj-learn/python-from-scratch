# DataFrame: A two-dimensional, labeled DATA structure with rows and columns.
# Series: A one-dimensional labeled array, similar to a column in a DataFrame.
# Rows: Horizontal records in a DataFrame, representing individual observations.
# Columns: Vertical records in a DataFrame, representing different variables.

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  # DataFrame
print(type(data["temp"]))  # Series
print()

temp_list = data["temp"].to_list()
print(temp_list)
print()

# Calculate the average temperature
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)
print(data["temp"].mean())  # With pandas
print()

# Max temperature
print(data["temp"].max())
print()

# Get Data in Columns
print(data["condition"])
print(data.condition)  # Pandas convert all header to attributes
print()

# How to get DATA in Row
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32  # Convert to fahrenheit
print(monday)
print(monday_temp)
print(monday_temp_F)
print()

# Print the row of DATA which had the highest temperature
print(data[data.temp == data["temp"].max()])
print(data[data.temp == data.temp.max()])  # Preferred way
print()

# Create dataframes from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [69, 56, 69]}
new_data = pandas.DataFrame(data_dict)  # Convert to DataFrame
new_data.to_csv("new_data_from_pandas.csv")  # Create CSV file from DataFrame
print(new_data)
