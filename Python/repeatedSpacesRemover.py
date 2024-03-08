"""
Create a program that reads a text file and eliminates repeated spaces between words and at the end
of the lines. The output file must also not have more than one blank line repeated
"""

wordList = []
with open("default_text.txt", "r") as read_archive:
    text = read_archive.readlines()
    BLANK_COUNTER = 0
    for line in text:
        if line == "\n":
            BLANK_COUNTER += 1
            if BLANK_COUNTER >= 2:
                pass
            else:
                wordList.append("\n")
        else:
            BLANK_COUNTER = 0

            COUNTER = 0
            while COUNTER < len(line):
                if line[COUNTER] == " " and line[COUNTER + 1] == " ":
                    COUNTER += 1
                else:
                    wordList.append(line[COUNTER])
                    COUNTER += 1
    print(">>finished reading<<")

with open("default_text.txt", "w") as write_archive:
    print(">>WRITING<<")
    for word in wordList:
        write_archive.write(word)
    print(">>END<<")

