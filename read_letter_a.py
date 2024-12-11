# Simple program to print lines with 'a'
with open('sample.txt', 'r') as file:
    for line in file:
        if 'a' in line:
            print(line.strip())
