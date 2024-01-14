"""
Using the type function, write a recursive function that prints the elements of a list.
Each element must be printed separately, one per line. Consider the case of lists within lists,
like "L = [1, [2, 3, 4, [5, 6, 7]]]". At each level, print the rightmost list, as we do when indenting
blocks in Python. Tip: send the current level as a parameter and use it to calculate the amount of
blank spaces to the left of each element.
"""

L = [1, [2, 3, 4, [5, 6, 7, 8]]]


def recursivePrinter(choosenList, level = 0):
    print(' ' * level)
    for element in choosenList:
        if type(element) is int:
            print(element, end='')
        elif type(element) is list:
            level += 5
            return recursivePrinter(element, level)
    print()


recursivePrinter(L, 0)










