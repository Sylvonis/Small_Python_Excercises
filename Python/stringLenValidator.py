# Write a function to validate a string variable. This function takes as a parameter, the string,
# the minimum and maximum number of characters. Return true if the length of the string is between
# the maximum and minimum values, and false otherwise

def stringValidator():

    stringminlen = int(input("Enter the minimum length of the string"))
    stringmaxlen = int(input("Enter the maximum length of the string"))

    while True:
        givenString = input("Enter your string. 2 to exit")
        if int(givenString) == 2:
            break
        if len(givenString) < stringminlen:
            print(f"This string should should have at minimum {stringminlen} characters long")
        if len(givenString) > stringmaxlen:
            print(f"This string should should have at maximum {stringmaxlen} characters long")
        if stringmaxlen >= len(givenString) >= stringminlen:
            print()
            print(1)
            print(f"{givenString} is valid\nIts lenght is sure between {stringminlen} and {stringmaxlen}")

stringValidator()








