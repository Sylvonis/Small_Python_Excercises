"""
write a generator capable of generating the sequence of prime numbers
"""


def primeNumberGenerator(max_range):
    i = 2
    while i < max_range:
        isprime = True
        for x in range(2, i):
            if i % x == 0:
                isprime = False

        if isprime is True:
            print(f"{i} is a prime number!")
            yield i
        i += 1


g = primeNumberGenerator(1000)  # save all the first 1000 first prime numbers


try:
    [next(g) for number in range(1000)]  # show the first 1000, if more than the saved, nothing happens because of try

except StopIteration:
    print('end')
    pass



