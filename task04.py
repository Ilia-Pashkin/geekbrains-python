rus = ["Один", "Два", "Три", "Четыре"]

text_file = open("file04.txt", "r").readlines()

for i in range(len(text_file)):
    text_file[i] = text_file[i].split(" — ")
    text_file[i][0] = rus[i]
    text_file[i] = (" — ".join(text_file[i]))

text_file = "".join(text_file)
print(text_file, file = open("file04-rus.txt", "w"))