# Table Printer
# Write a function named printTable() that takes a list of lists of strings and displays it in
# a well-organized table with each column right-justified. Assume that all the inner lists will
# contain the same number of strings. For example, the value could look like this:
#
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
#
# Your printTable() function would print the following:
#
#    apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose
#
# Hint: your code will first have to find the longest string in each of the inner lists so that
# the whole column can be wide enough to fit all the strings. You can store the maximum
# width of each column as a list of integers. The printTable() function can begin with
# colWidths = [0] * len(tableData), which will create a list containing the same number
# of 0 values as the number of inner lists in tableData. That way, colWidths[0] can store
# the width of the longest string in tableData[0], colWidths[1] can store the width of the
# longest string in tableData[1], and so on. You can then find the largest value in the
# colWidths list to find out what integer width to pass to the rjust() string method.

# Note: This one i didn't quite unsdertand how it works, this was so f****** hard
#       and this ins't good, i'll come back later and understand better #22/09/2023#

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def table_printer(tab_data):
    col_widths = [0] * len(tab_data)    # returns 3 lists with [0, 0, 0]
    #print(range(len(max(tab_data[0]))))
    for j in range(len(tab_data[0])):   # for each table(j) lenght in the range of tab_data
        for i in range(len(tab_data)):  # for each item(i) lenght in the range of tab_data
            col_widths[i] = len(max(tab_data[i], key=len))  # return the bigest(max) item(i) lenght value in tab_data.
                                                            # key=len tranforms each value to the lengh of characters
            a = tab_data[i][j]
            print(a.rjust(col_widths[i]), end=' ')
        print('\n')

table_printer(tableData)










