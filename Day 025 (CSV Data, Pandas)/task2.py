import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

#Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in row
# print(data[data.day == "Monday"])
# print(type())
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)

#Create a dataframe from scratch 

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores" : [76,56,65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")