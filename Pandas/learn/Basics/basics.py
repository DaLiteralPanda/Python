import pandas as pd

# Two main data types

# Series
# Series take in a Python List
series = pd.Series(["BMW", "Toyota", "Honda"])
# Viewing the series
series
# Series are 1 dimensional(1-D)

colors = pd.Series(["Red", "Blue", "White"])
colors

# DataFrame is 2-dimensional(2-D)
# DataFrames take in a Python Dictionary
# Beautify thing about DataFrame is that you can create a DataFrame from a series
car_data = pd.DataFrame({"Car make": series, "Color": colors})
car_data

# Import Data
# Takes files(data) like, .excel .csv(comma seperated values) etc.

car_sales = pd.read_csv("./data/car-sales.csv")
car_sales

# Exporting a DataFrame
# Take the variable and then use the method .to_csv and type file name in the brackets(and quotes)

car_sales.to_csv("exported-car-sales.csv", index=False) # If you dont put "index=False" it will export with the index values
# CSV is a univeral datatype
