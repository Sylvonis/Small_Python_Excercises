"""
Part 1: write a program that receives the name of a file from the command line and
print all lines of this file

Part 2: modify the program from the previous exercise so that it receives two more
parameters: the start line and the end for printing. The program should only print
the lines between these two values (including start and end lines)
"""

def printer(i):
    for __ in range(i):
        print()


def fileReader(file_str, start=0, end=0):
    f = open(f"{file_str}.txt", "r")
    i = 1
    while start > i:
        f.readline()
        i += 1
    while end >= i:
        print(f.readline().strip())
        i += 1
    f.close()


choosen_file = input("Write the name of the file you want to print (only file name, no format)\n")
printer(2)
min_range = int(input("Choose the line starting point (which line to start reading)\n"))

while True:
    max_range = int(input("Choose the line ending point (which line to stop reading)\n"))
    if max_range >= min_range:
        break
    print(f"Ending point can't be smaller than the starting point.\nChosen starting point = {min_range}")

printer(3)
fileReader(choosen_file, int(min_range), int(max_range))

