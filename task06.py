my_dict = {}
print(type(my_dict))

text_file = open("file06.txt", "r").readlines()
for i in range(len(text_file)):
    my_dict.update({text_file[i].split(": ")[0]: [text_file[i].split(" ")[j] for j in range(1, len(text_file[i].split(" ")))]})
for key in my_dict:
    i = 0
    while i < len(my_dict[key]):
        my_dict[key][i] = "".join([symbol for symbol in my_dict[key][i] if symbol.isdigit()])
        try:
            my_dict[key][i] = int(my_dict[key][i])
            i += 1
        except:
            del my_dict[key][i]

    while len(my_dict[key]) > 1:
        my_dict[key][0] += my_dict[key][1]
        del my_dict[key][1]

    my_dict[key] = my_dict[key][0]

print(my_dict)