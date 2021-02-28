my_list = input().split()
l = len(my_list)
my_list = "\n".join(my_list)

text_file = open("file05.txt", "w")
text_file.write(my_list)
text_file.close()
text_file = open("file05.txt", "r")

sum = 0
for line in text_file:
    sum += int(line)

print(f"Сумма чисел в файле: {sum}")