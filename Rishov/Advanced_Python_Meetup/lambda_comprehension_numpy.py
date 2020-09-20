import numpy as np
import pandas as pd

np.random.random((2, 2))

data_gen = lambda m, n: np.random.random((m, n))
data_gen(3, 3)

my_arr = data_gen(3, 2)
my_arr
my_arr[0]

my_arr_2 = []

for i in range(2):
    row_list = [np.random.random() for j in range(2)]
    my_arr_2.append(row_list)

my_arr_2

my_arr_2[0:][0]

# Dict Comprehension

data2transform = data_gen(200, 5)
data2transform.shape
data2transform.shape[1]

transformed_dict = {}
for i in range(data2transform.shape[1]):
    transformed_dict[f"column_{i+1}"] = data2transform[:, i]

transformed_dict['column_1'].shape

pd.DataFrame.from_dict(transformed_dict)

pd.DataFrame.from_dict({f"column_{i+1}": data2transform[:, i] for i in range(data2transform.shape[1])})

# Same task by pasing array directly to df

pd.DataFrame(data2transform, columns=[f"column_{i+1}" for i in range(data2transform.shape[1])])
