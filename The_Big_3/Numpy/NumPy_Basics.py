import numpy as np

# 1D
x = np.linspace(1,10,num=10)
print(x.shape)
print(x)

# 2D
print(x.reshape(5,2))
# The first one is the rows second one is the columns
# So to do 5 rows and 2 columns you will need to divide 10 by 2 to get 5 and then 2 columns
print(type(x))
# Create a list and transform it into a matrix
my_list = [i for i in range(15)]
my_list = np.array(my_list).reshape(5,3)
print(my_list)



### Solving Linear Equations with numpy

## 3x_0 + x_1 = 9
## x_0 + 2x_1 = 8

# One way
a = np.array([[3,1],[1,2]])
print(a.shape)

# Otehr way
a = np.array([3,1,1,2])
print(a.reshape(2,2))
b = np.array([9,8])
print(b)
# Solution
print(np.linalg.solve(a.reshape(2,2),b))
# Means x_0 is equal to 2 and x_1 is equal to 3

### Creating function for doing this for any equation

class Linear():
    def __init__(self, x,y):
        self.x = np.array(x).reshape(2,2)
        self.y = np.array(y)

    def solve(self):
        return np.linalg.solve(self.x, self.y)

result = Linear([3,1,1,2], [9,8])
print(result.solve())
print(type(result))
