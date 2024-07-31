import csv

with open("weather_data.csv") as csvfile:
    data = csv.reader(csvfile)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
