import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Data.csv")
squirrel_colors = data["Primary Fur Color"]

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])



data_dict = {
    "Fur Color": ["gray","red","black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}


squirrel_data = pandas.DataFrame(data_dict)
squirrel_data.to_csv("squirrel_count.csv")