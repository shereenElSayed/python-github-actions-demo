from operator import mul
from functools import reduce 

def multiply(values,):
    return reduce(mul, values, 1)

def summation(values):
    return sum(values)

def print_result(operation, result):
    print(f'Your {operation} operation result = {result}')