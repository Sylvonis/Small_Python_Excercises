"""
Write a function that takes a string and a list. The function must compare the passed string with the elements
in the list, also passed as a parameter. Return true if the string is found within the list, and false otherwise
"""
listOfChars = []


def listCreator():
    while True:
        print("list: ", listOfChars)
        inputStr = input("Type a String to add to the list. Type 'exit' to stop\n")
        if inputStr.upper() == "exit".upper():
            break
        listOfChars.append(inputStr)


def checkStringFromList(list):
    string = input("Type the string you want to find\n\n")
    pos = 0
    while pos < len(list):
        if list[pos].upper() == string.upper():
            print(f"{string} is in the list on position {pos}")
            return string, pos
        pos += 1
    print("String not found")


listCreator()
print(checkStringFromList(listOfChars))

