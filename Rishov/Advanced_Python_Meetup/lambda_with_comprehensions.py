# Lambda Exprensions

## Follows event-driven programming paradigm
## Anonymous functions in Python
## Clean and consise code
## Pairs well with iterable methods

def fname2(x):
    return 2*x

fname = lambda x: 2*x

fname(4)

# List with numbers 1 to 100

my_list = [i for i in range(1, 101)]

# Example of applying function to elements in list comprehensions
f_list = [fname(i) for i in my_list]

# Using map

# Create the above list using map and lambda
f_list_2 = map(lambda x:2*x, my_list)
f_list_2

list(f_list_2)

# map(function exprension, args)

# 2x^2 + 4x + 4

poly = lambda x:2*x**2 + 4*x + 4

[poly(i) for i in my_list if poly(i) > 50]

# Filter, Map and Lambda
final_vals = list(filter(lambda x: x > 50, map(lambda x: 2*x**2 + 4*x + 4, my_list)))


# Reduce()
from functools import reduce

reduce(lambda x, y: x+y, final_vals)
