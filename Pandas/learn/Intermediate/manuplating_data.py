import pandas as pd

# If your root directory is "learn" then run this
car_sales = pd.read_csv("./data/car-sales.csv")
# If not run this (Uncomment it ofc lmao)
# car_sales = pd.read_csv("../data/car-sales.csv")


## Manuplating Data

# Lowers text
car_sales.Make.str.lower()

# If you want to change a column it requires resigning like this
car_sales["Make"] = car_sales["Make"].str.lower()
car_sales.head()

# Getting a dataset with missing data
# Real datasets have missing data

# If your root directory is "learn" then run this
car_sales_missing = pd.read_csv("./data/car-sales-missing-data.csv")
# If not run this (Uncomment it ofc lmao)
# car_sales_missing = pd.read_csv("../data/car-sales-missing-data.csv")

# "NaN" = there is no value
car_sales_missing

# Fill a cell with some data
car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean())
# What this says is that
#### Fill the Odometer Missing Values("NaN") with the mean of the Odometer Filled Cells
car_sales_missing.head()

# Inplace
#### The inplace argument is set to "False" by default but we can make it "True"
#### and then stop resigning if we dont wanna do that
car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean(), inplace=True)
car_sales_missing.head()

# Removes the missing values("NaN" Ones)
car_sales_missing.dropna()
car_sales_missing
car_sales_missing.dropna(inplace=True)
car_sales_missing

car_sales_missing_dropped = car_sales_missing.dropna()
car_sales_missing_dropped

# Column form Series
seats_columns = pd.Series([5, 5, 5, 5, 5])

# Making a new column
# New Column called Seats
car_sales["Seats"] = seats_columns
car_sales
# Filling the missing Values
car_sales["Seats"].fillna(5, inplace=True)
car_sales

# Column form list
fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 5.6, 1.2, 45.6, 6, 7]
car_sales["Fuel per 100KM"] = fuel_economy
car_sales

# Figuring out how much fuel a car has used in its enitre life
car_sales["Total Fuel Used"] = car_sales["Odometer (KM)"]/100 * car_sales["Fuel per 100KM"]
car_sales

# Create a column from a single value
car_sales["Number of wheels"] = 4
car_sales

# Bolean column
car_sales["Passed road safety"] = True
car_sales
car_sales.dtypes

# Removing a column
car_sales = car_sales.drop("Total Fuel Used", axis=1)
car_sales
