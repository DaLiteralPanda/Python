import pandas as pd

car_sales = pd.read_csv("./data/car-sales.csv")

# Returns the first 5 rows of your DataFrame
car_sales.head()
# Type in a number to return that many rows
car_sales.head(7)

# Tells the bottom 5 rows of your DataFrame
car_sales.tail()
# Again same thing
car_sales.tail(3)

# .loc # .iloc
animals = pd.Series(["PANDAZZZ", "#savethepandas", "Toucan", "Inland Viper", "Penguin"], index=[0, 3, 9, 8, 3]) # Custom Index
animals
# .loc = location
animals.loc[3]
# So, it refers to the index numbers
animals.loc[9]

car_sales.loc[3]

# .iloc = position
# So it gives us the position
animals.iloc[3]
animals

car_sales.iloc[3]
# Its same

# Slicing with .iloc and .loc

animals.iloc[:3]

car_sales.loc[:3]


# Will show the exact same thing
car_sales["Make"]

car_sales.Make
# If your column name has a space in it the dot(".") notation wont work

# I only want the data in the make column which is equal to Toyota
car_sales[car_sales["Make"] == "Toyota"]
car_sales[car_sales["Odometer (KM)"] > 100000]

# Compare two columns

pd.crosstab(car_sales.Make, car_sales.Doors)

# Compare more columns in the context of another
car_sales.groupby(["Make"]).mean()
car_sales.groupby(["Colour"]).mean()

# Making a plot
# Line Chart (Graph)
car_sales["Odometer (KM)"].plot()

# Histogram
car_sales["Odometer (KM)"].hist()

# Converting a Price Column to and integer column
# (Column with $ Signs that looks like an "int" but its actually an "object" according to pandas anyways hehe)

car_sales['Price'] = car_sales['Price'].str.replace('[\$\,]', '').astype(float)
car_sales['Price'].plot()
