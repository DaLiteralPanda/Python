# Comprehensions

## Clean and consise code
## Fast and Efficient Performance
## Applies to list, dicts, sets, and generators exprensions

nums = [1, 2, 3]

for i in nums:
    print(i)
i

def num_print(num_list):
    for i in num_list:
        print(i)

# Restart now
i #error

# List comprehension

## What if we wanted a list in which you can double each number from 1 to 100

# Normal loop
double_num = []

for num in range(1, 101):
    double_num.append(2*num)

double_num

# List comprehension
double_num_two = [2*num for num in range(1, 101)]

# restart now
num

my_vals = [i for i in range(1, 101)]

final_dict = {}

## Have to create 10 diff keys Col_1 ... Col_10
## Col_1 :[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and etc

cols = [(i, val) for i, val in enumerate(list(range(1, 11)))]

val_slice_list = [i for i in range(10)]

# Normal way

# Stuff here

for i, slice in enumerate(val_slice_list):
    final_dict[f"Col_{i+1}"] = slice

# Comprehensions

my_dict_comp = {f"Col_{i+1}" : slice for i, slice in enumerate(val_slice_lis)}

## 1 - 100 => x^2 + 4x + 4

def my_polynomial(x):
    return x**2 + 4*x + 4

pol_complete = [my_polynomial(i) for i in range(1, 101)]

my_pol_dict = {f"{i + 1}": slice for i, slice in enumerate(pol_complete)}
my_pol_dict

# Set comprehensions

# Normal method
my_abs_list = []

for i in range(-1000, 1001):
    val = abs(i)
    my_abs_list.append(val)

# USing it with list comprehension
set([abs(i) for i in range(-1000, 1001)])

{abs(i) for i in range(-1000, 1001)} # Set comprehension

# Finding the mean of numbers from 1 to 1000

sum([i for i in range(1, 101)]) / len([i for i in range(1, 101)])
