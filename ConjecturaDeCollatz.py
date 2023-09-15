
def collatz(number):

    while number != 1:

        print(number)

        if number % 2 == 0:
            number = number // 2

        elif number % 2 == 1:
            number = 3 * number + 1

try:
    collatz(int(input("input a integer number")))

except ValueError:
    print('we only accept integer numbers. try again')


