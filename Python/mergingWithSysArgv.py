"""
create a program that takes the name of two files as command line parameters and generates a
output file with lines from the first and second file
"""

import sys
from mergingTwoLists import numericOrderMerge

a = sys.argv[1]
b = sys.argv[2]

numericOrderMerge(a, b)