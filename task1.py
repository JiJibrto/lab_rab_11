# !/usr/bin/evn python3
# -*- config: utf-8 -*-

import timeit


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    comm = int(input("Enter number> "))
    r_fib = fib(comm)
    r_factorial = factorial(comm)

    print(timeit.timeit("r_factorial", setup="from __main__ import r_factorial"))
    print(timeit.timeit("r_fib", setup="from __main__ import r_fib"))