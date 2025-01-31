
import pandas

# squirrel_whole_data = pandas.read_csv("day-25\\squirrels\\squirrel_count.csv")
# squirrel_furs = squirrel_whole_data["Primary Fur Color"]
# squirrel_fur_dict:dict[str,int] = {}

# for squirrel_fur in squirrel_furs.unique().tolist():
#     if squirrel_fur == "nan":
#         squirrel_fur_dict["nan"] = squirrel_whole_data.count("nan")
#     else:
#         squirrel_fur_dict[squirrel_fur] = squirrel_furs.tolist().count(squirrel_fur)

# print(squirrel_fur_dict.keys(), squirrel_fur_dict.values())
# print(pandas.DataFrame(list(squirrel_fur_dict.items()),columns=["fur", "count"]))


# ====================================================================
# from video

data = pandas.read_csv("day-25\\squirrels\\squirrel_count.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)

data_dict = { "Fur Color":["Gray", "Cinnamon", "Black"],
             "Count": [grey_squirrels,red_squirrels,black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("day-25\\squirrels\\fur_squirrel_count.csv")