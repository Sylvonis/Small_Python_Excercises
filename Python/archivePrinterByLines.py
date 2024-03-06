"""
Create a program that prints lines from a file. This program must receive three parameters through the
command line: file name, starting line and last line to print
"""


def lineAndNameVerifier(archive):
    LINE_COUNT = 0
    try:
        with open(archive + ".txt") as arch:
            lines = arch.readlines()
            LINE_COUNT = 0
            for line in lines:
                LINE_COUNT += 1
        return LINE_COUNT
    except FileNotFoundError:
        print(f">>>> The file {archive} does not exist <<<<")
        i = input("Write the archive name to print")
        return lineAndNameVerifier(i)


def archivePrinter(archive):
    LINES = lineAndNameVerifier(archive)
    with open(archive + ".txt") as arch:
        while True:
            START_LINE = int(input(f"Input the line you want to start printing\n\nNumber of Lines: {LINES}\n"))
            if int(START_LINE) < 1 or int(START_LINE) > LINES:
                print(f"\n\n\n\n\nThe starting line must be between 0 and {LINES}\n")
            else:
                break
        while True:
            END_LINE = int(input(f"Input the line you want to end printing\n\nNumber of Lines: {LINES}\n"))
            if int(END_LINE) < 1 or int(END_LINE) > LINES:
                print(f"\n\n\n\n\nThe starting line must be between 0 and {LINES}\n")
            else:
                print("\n\n\n\n")
                break
        lineList = []
        for line in arch.readlines():
            lineList.append(line.strip())
        for line in enumerate(lineList, start=1):
            if START_LINE <= int(line[0]) <= END_LINE:
                print(line[1])
        print(f"\n>>> Printed Lines between {START_LINE} and {END_LINE}")


archivePrinter(input("Write the archive name to print\n"))










