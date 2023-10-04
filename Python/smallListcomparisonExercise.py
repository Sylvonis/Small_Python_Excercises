"""
 1 - Escreva um programa que compare duas listas. Utilizando operações com conjuntos imprime:

    * os valores comuns ás duas listas *
    * os valores que só existem na primeira *
    * os valores que exstem apenas na segunda *
    * uma lista com os elementos, não repetidos, das duas listas
    * a primeira lsta sem os elementos repetidos na segunda

 2 - Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial
    e a segunda como a versão após alterações. Utilizando operações com conjuntos seu programa deverá
    imprimir a lista de modificações entre essas duas versões, listando:

    * os elementos que não mudaram
    * os novos elementos
    * os elementos que foram removidos

"""


def compareLists(x, y):
    common_values = set()
    x_only_values = set()
    y_only_values = set()
    z_list = set()
    non_rep_x_values = set()

    for value in x:
        z_list.add(value)
        x_only_values.add(value)
        if value in y:
            common_values.add(value)
        if value not in y:
            non_rep_x_values.add(value)

    for value in y:
        y_only_values.add(value)
        if value in x:
            pass
        if value not in z_list:
            z_list.add(value)

    print(f'{x} is the first list')
    print(f'{y} is the second list\n')
    print(f'{common_values} are common values')
    print(f'{x_only_values} are values only from the first list'),
    print(f'{y_only_values} are values only from the second list'),
    print(f'{z_list} are the, non repeated, values from both lists')
    print(f'{non_rep_x_values} is the first list without the repeated values from the second\n\n')


def listUpdated(x, y):
    no_changes = set()
    added_value = set()
    removed_value = set()

    for value in y:
        if value in x:
            no_changes.add(value)

        elif value not in x:
            added_value.add(value)

    for value in x:
        if value not in y:
            removed_value.add(value)

    if no_changes == set():
        pass
    else:
        print(f'{no_changes} are unchanged')

    if added_value == set():
        pass
    else:
        print(f'{added_value} was added')

    if removed_value == set():
        pass
    else:
        print(f'{removed_value} was removed\n\n')


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = [1, 2, 3, 4]
d = [1, 3, 4, 5, 6]

listUpdated(a, b)
compareLists(a, b)
