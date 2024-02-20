#!/usr/bin/python3

from math import floor, sqrt

def factorize(n):
    # since even nos. are always divisible by 2, one of the factors will always
    # be 2
    if (n & 1) == 0:
        return (n/2, 2)

    a = floor(sqrt(n))

    # if n is a perfect square the factors will be ( sqrt(n), sqrt(n) )
    if a * a == n:
        return (a, a)

    # n = (a - b) * (a + b)
    # n = a^2 - b^2
    # b^2 = a^2 - n
    while True:
        a += 1
        _b = a * a - n
        b = int(sqrt(_b))
        if (b * b == _b):
            break

    return (a + b, a - b)

print(factorize(105327569))