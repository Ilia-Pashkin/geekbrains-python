import json

profit = []
firms = []
dict_profit = {}
dict_average = {}

text_file = open("file07.txt", "r").readlines()
for i in range(len(text_file)):
    text_file[i] = text_file[i].split(" ")
    firms.append(text_file[i][0])
    profit.append(int(text_file[i][2]) - int(text_file[i][3]))

for i in range(len(text_file)):
    dict_profit.update({firms[i]: profit[i]})

dict_average = {"Average profit": sum([profit[i] for i in range(len(profit)) if profit[i] >= 0]) / len([profit[i] for i in range(len(profit)) if profit[i] >= 0])}

my_list = []
my_list.append(dict_profit)
my_list.append(dict_average)

with open("file07save.json", "w") as json_obj:
    json.dump(my_list, json_obj)