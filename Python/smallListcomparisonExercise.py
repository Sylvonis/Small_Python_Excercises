
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]


def compareLists(x, y):
    common_values = []
    x_only_values = []
    y_only_values = []
    z_list = []
    non_rep_x_values = []

    for value in x:
        z_list.append(value)
        x_only_values.append(value)
        if value in y:
            common_values.append(value)
        if value not in y:
            non_rep_x_values.append(value)

    for value in y:
        y_only_values.append(value)
        if value in x:
            pass
        if value not in z_list:
            z_list.append(value)

    print(f'{x} is the first list')
    print(f'{y} is the second list\n')
    print(f'{common_values} are common values')
    print(f'{x_only_values} are values only from the first list'),
    print(f'{y_only_values} are values only from the second list'),
    print(f'{z_list} are the, non repeated, values from both lists')
    print(f'{non_rep_x_values} is the first list without the repeated values from the second')


compareLists(a, b)