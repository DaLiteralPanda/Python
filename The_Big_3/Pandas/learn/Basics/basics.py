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


# Describe Data in Pandas

# Attributes
# Describing DataTypes
car_sales.dtypes # Its an attribute as it dosent have "()" after it # A Function does have () after it

# Tells us our column names
car_sales.columns

# Tells us about the index (range of it)
car_sales.index

# Functions

# Gives us some statical info about our numeric columns
car_sales.describe()

# Gives us all sorts of information
car_sales.info()

# Gives the average of the numeracial columns
car_sales.mean()
# You can even call it on individual series
car_prices = pd.Series([3000, 1500, 111250])
car_prices.mean()

car_sales.sum()

# Selecting a single column
car_sales["Doors"].sum()

# Tells the number of rows
len(car_sales)
