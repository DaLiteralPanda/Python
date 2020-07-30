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
# Bar Plot (my expirement)
car_sales.plot(x="Sale Date", y="Total Sales", kind="bar");
# Hist Plot (my expeiremnt)
car_sales.plot(x="Make", y="Price", kind="hist");

# How about a bar plot?
x = np.random.rand(10, 4)
x[:5]
# Turn it into a dataframe
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])
df
df.plot.bar();
# Different way
df.plot(kind="bar");

# Plotting the csv (data)
car_sales.plot(x="Make", y="Odometer (KM)", kind="bar");

# How about Histograms?

car_sales["Odometer (KM)"].plot.hist();
car_sales["Odometer (KM)"].plot(kind="hist");

# Adjusting the bin size
car_sales["Odometer (KM)"].plot.hist(bins=10);

# Lets try another dataset
heart_disease = pd.read_csv("./data/heart-disease.csv")
heart_disease.head()

# Create a Histogram of age
heart_disease["age"].plot.hist(bins=10);

heart_disease.head()
heart_disease.plot.hist(figsize=(10, 30), subplots=True);
# Not a good plot

### Which one to use? (pyplot vs matplotlib OO method)

# When plotting something quickly, okay to use pyplot method
# When plotting something more advanced use OO method

##### OO = Object Oriented (oobviously lmaoo)

# OO Method
over_50 = heart_disease[heart_disease["age"] > 50]
len(over_50)

# Scatter Plot

# Pyplot method
## We want the age and colestrol but we want to colour it with the flavous of the target column
over_50.plot(kind="scatter", x='age', y='chol', c='target', figsize=(10, 6)); # c == colour
# Not a good plot in this senario

over_50.tail()

# OO method mised with pyplot Method
fig, ax = plt.subplots(figsize=(10, 6))
over_50.plot(kind="scatter", x='age', y="chol", c="target", ax=ax);
#ax.set_xlim([45, 100]);

# OO method from scratch
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
scatter = ax.scatter(x=over_50["age"], y=over_50["chol"], c=over_50["target"]);

# Customize it
ax.set(title="Heart Disease and Cholesterol Levels", xlabel="Age", ylabel="Cholesterol");

# Add a legend
ax.legend(*scatter.legend_elements(), title="Target");

# Add a horizantal line
ax.axhline(over_50["chol"].mean(), linestyle='--');
