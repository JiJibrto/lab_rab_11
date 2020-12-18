# !/usr/bin/evn python3
# -*- config: utf-8 -*-

import timeit


def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    comm = int(input("Enter number> "))
    r_fib = fib(comm)
    r_factorial = factorial(comm)

    print(timeit.timeit("r_factorial", setup="from __main__ import r_factorial"))
    print(timeit.timeit("r_fib", setup="from __main__ import r_fib"))
