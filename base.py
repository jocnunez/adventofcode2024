FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as file:
    for line in file:
        print(line.strip())