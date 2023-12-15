"""
This function will return the given position of your choosen Fibonacci value
Example:
    55 is the value in the 10º position
"""


def truefibonacci(n):
    v1 = 1
    v2 = 1
    Count = 1

    while Count < n:
        v3 = v1 + v2
        v1 = v2
        v2 = v3
        Count += 1
    return v1


def recursiveFibonacci(n):
    if n <= 1:
        return n
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)


print(recursiveFibonacci(15))
print(truefibonacci(15))



