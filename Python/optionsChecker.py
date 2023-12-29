"""
Write a function that receives a string with valid options to accept (each option is a letter).
Convert valid options to lowercase letters, use input to read an option, convert the value to
lowercase letters and check if the option is valid. In case of an invalid option, the function
must ask the user to re-enter another option
"""

valueStr = input("Write the string you want to use:\n\n")


def optionsChecker(string):
    newList = []

    for char in string:
        newList.append(char.lower())
    print("List: ", newList)

    while True:
        inputLetter = input("Enter a letter to check:\n\n\n")
        if inputLetter.lower() in newList:
            print("That's a valid Option!")
            break
        else:
            print('That option is invalid...')


optionsChecker(valueStr)
