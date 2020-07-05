# Map Demo

# List of Numbers
nums = [2,7,11,15]

# Create a function to add 3 to a number
def add_three(x):
  return x + 3

# Use map to create a list of each number added by 3
x = map(add_three, nums)
x = list(x)
print(x)
