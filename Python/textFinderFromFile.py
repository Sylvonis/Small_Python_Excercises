"""
This is just a word finder that I made while studying regular expressions

You input a word/value/number and the program finds the values in the default_text.txt, show to you the value
and in which line it was found

The default text is just the Lorem Ipsum default text that you can find anywhere in the internet
"""

import re

lineNumber = 1
found_COUNTER = 0
found = False


DEFAULT_TEXT = open('default_text.txt', 'r')
input_WORD = input('input a word to find: \n')

value = re.compile(r'\s' + input_WORD + r'\s')


for line in DEFAULT_TEXT:
    found_VALUE = re.findall(value, line)

    for value in found_VALUE:
        found_COUNTER += 1

    if found_VALUE:
        print('found ' + str(found_COUNTER) + ' of the matching value: ' + str(found_VALUE) +
              '\non line: ' + str(lineNumber))
        print()
        found = True
    lineNumber += 1
    found_COUNTER = 0


if not found:
    print('No value has been found')

