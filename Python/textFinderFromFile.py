"""
This is just a word finder that I made while studying regular expressions

You input a word/value/number and the program finds the values in the default_text.txt, show to you the value
and in which line it was found. The program does differentiate lower case and upper case, so Et and et both
have different results

The default text is just the Lorem Ipsum default text that you can find anywhere in the internet
"""

import re

DEFAULT_TEXT = open('default_text.txt', 'r')
DEFAULT_TEXT2 = open('default_text2.txt', 'r')

input_WORD = input('input a word to find: \n')
value = re.compile(r'\s' + input_WORD + r'\s')


def wordFinder(word, text_var):
    line_number = 1
    found_counter = 0
    found = False

    for line in text_var:
        found_value = re.search(word, line)
        found_value_string = re.findall(word, line)

        for __ in found_value_string:
            found_counter += 1

        if found_value:
            print('found ' + str(found_counter) + ' of the matching value: ' + str(found_value.group()) +
                  '\non line: ' + str(line_number))
            print()
            found = True
        line_number += 1
        found_counter = 0

    if not found:
        print('No value has been found')


wordFinder(value, DEFAULT_TEXT)
