with open("file01.txt", "w") as text_file:
    while True:
        line = input()
        if line != "":
            text_file.write(line + '\n')
        else:
            break