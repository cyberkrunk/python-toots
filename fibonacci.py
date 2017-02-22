#!/bin/usr/env python3

# Function to return Fibonacci series up to n
# fib3 is a version of fib1
def fib3(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


# Function to return first n numbers of the fibonacci series
def fib2(n):
    result = []
    a, b = 0, 1
    count = 1
    while count <= n:
        result.append(b)
        a, b = b, a+b
        count += 1
    return result

print(fib2(20))

print(fib3(65536))

