"""
write a generator capable of generating the sequence of prime numbers
"""


g = [x for x in range(10)]


def isPrime(number):
    isprime = True

    if number == 0:
        print("Zero is not a prime number")
        return False
    if number == 1:
        print("One is not a prime number")
        return False
    if number < 0:
        print("A negative number can not be prime number")
        return False

    for x in range(2, number):
        if number % x == 0:
            isprime = False

    if isprime is False:
        print(f"{number} is not a prime number")
        return False
    elif isprime is True:
        print(f"{number} is a prime number!")
        return True


# def givePrimeNum(choosen_range):
#     for number in range(choosen_range):



# for each number in the sequence, divide it by all values before .index(number)
















