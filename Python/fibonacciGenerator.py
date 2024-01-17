"""
write a generator capable of generating the fibonacci sequence
"""

def truefibonacci(n):
    v1 = 1
    v2 = 1
    Count = 0

    while Count < n:
        v3 = v1 + v2
        v1 = v2
        v2 = v3
        Count += 1
        print(v1)
        yield v1

g = truefibonacci(100)

[next(g) for x in range(200)]






