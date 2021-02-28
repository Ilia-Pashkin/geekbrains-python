workers = []
salaries = []

text_file = open("file03.txt", "r").readlines()
for line in text_file:
    workers.append(line.split(" - ")[0])
    salaries.append(line.split(" - ")[1])

for i in range(len(salaries)):
    salaries[i] = int(''.join(salaries[i]))

print(f"Работники, у которых зарплаты ниже 20000: {[workers[i] for i in range(len(workers)) if salaries[i] < 20000]}")
print(f"Средняя зарплата работников: {round(sum(salaries) / len(salaries), 2)}")