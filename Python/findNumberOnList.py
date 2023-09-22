"""

This is just a program that finds a value within a list and returns the position it was found
and which value was found first

"""

number_List = [15, 7, 27, 39, 2]

num_value_1 = None
num_value_2 = None


while num_value_1 is None:
    try:
        num_value_1 = int(input("Input the first number you want to find:\n"))
    except:
        pass


while num_value_2 is None:
    try:
        num_value_2 = int(input("Input the second number you want to find:\n"))
    except:
        pass




def numberFinder(lista):
    num_position = 0
    found_first = 0
    found_value_1 = False
    found_value_2 = False
    print("\n"*5)

    for __ in lista:
        if num_value_1 == lista[num_position]:
            found_value_1 = True
            print(f"value {num_value_1} was found on position {num_position}")
            if found_first == 0:
                found_first = 1
                print(f"value {num_value_1} was found first!\n")
            else:
                pass
        elif num_value_2 == lista[num_position]:
            found_value_2 = True
            print(f"value {num_value_2} was found on position {num_position}")
            if found_first == 0:
                found_first = 2
                print(f"value {num_value_2} was found first!\n")
            else:
                pass
        num_position += 1
    if not found_value_1 and not found_value_2:
        print(f"Both values weren't found")
    elif not found_value_1:
        print(f'{num_value_1} was not found\n')
    elif not found_value_2:
        print(f'{num_value_2} was not found\n')



numberFinder(number_List)
