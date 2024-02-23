"""
    Create a program that reads a text file and generates a paged output file.
    Each line must contain no more than 76 characters. Each page will have a maximum of 60
    lines. Add the current page number and name to the last line of each page.
    of the original file.
"""

with open("TestsArchive.txt", "r") as text, open("OutputArchive.txt", "w") as output:
    CHAR = 0
    LINE = 0
    PAGE = 1
    for line in text.readlines():
        for char in line.strip():
            if CHAR == 60:
                output.write(f"\n")
                CHAR = 0
                if LINE >= 60:
                    output.write(f"\n{PAGE}" + "arquivo".center(54))
                    output.write("\n\n\n\n\n\n\n")
                    LINE = 0
                    PAGE += 1
                LINE += 1
            output.write(char)
            CHAR += 1
    if LINE < 60 and LINE != 0:
        output.write(f"\n\n{PAGE}" + "arquivo".center(54))
    pass





