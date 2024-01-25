

"""create a program that reverses the order of the lines in the pares.txt file. The first line must contain the
higher number; and the last, the smallest"""


def archiveLinesReverser(archive):
    num_list = []
    with open(f"{archive}.txt", "r") as file:
        for line in file.readlines():
            num_list.append(line.strip())

    with open(f"{archive}.txt", "w") as file:
        i = -1
        for n in num_list:
            file.write(num_list[i] + "\n")
            print(num_list[i])
            i -= 1


archiveLinesReverser("pares")   # write without ".txt"











