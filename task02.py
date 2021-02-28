i = 0
words_in_line = []

text_file = open("file02.txt", "r").readlines()
for line in text_file:
    words_in_line.append(line.count(' ') + 1)
    i += 1

print("Номер строки - число слов")
for j in range(i):
    print(f"{j+1} - {words_in_line[j]}")