import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

# Making a dataframe
car_sales = pd.read_csv("./data/car-sales.csv")

# Making a sample plot
ts = pd.Series(np.random.randn(1000), index=pd.date_range("29/07/2020", periods=1000))

ts = ts.cumsum() # Adds the last colum to the next one and repeat
ts.plot();

# Plotting from dataframe
car_sales["Price"] = car_sales["Price"].str.replace('[\$\,]', '').astype(float)
car_sales

car_sales["Sale Date"] = pd.date_range("01/01/2020", periods=len(car_sales))
car_sales.head()
car_sales["Total Sales"] = car_sales["Price"].cumsum()
car_sales

# Lets plot "Total Sales"
car_sales.plot(x="Sale Date", y="Total Sales");
# Scatter Plot
car_sales.plot(x="Odometer (KM)", y="Price", kind="scatter");
# Bar Plot
car_sales.plot(x="Sale Date", y="Total Sales", kind="bar");
# Hist Plot
car_sales.plot(x="Make", y="Price", kind="hist");
