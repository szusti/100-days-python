import os
import csv
# need to install pandas separately
# py -m pip install pandas
import pandas

# data:list[str] = []
# with open("day-25\\weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# with open("day-25\\weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures:list[int] = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(row[1])

# print(temperatures)

# data = pandas.read_csv("day-25\\weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print("Temp in Farehneit",(monday.temp.to_list()[0]) *9/5 + 32)

# create dataframe from scratch

data_dict = {
    "students": ["Amy", 'James', "Angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("day-25\\panda-module\\new_data.csv")
