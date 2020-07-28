import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

### Making figures with NumPy arrays

# Create some data

x = np.linspace(0, 10, 100) # Start, Stop, Num
# Returns evenly spaced values between the given paramaters
# This code gives a 100 evenly spaced values between 0 and 10
x[:10]

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, x**2);
# Default plot in matplotlib is a line plot

# Create a Scatter plot
fig, ax = plt.subplots()
ax.scatter(x, np.exp(x));
# np.exp, Calculates the exponential of all elements in the input array

fig, ax = plt.subplots()
ax.scatter(x, np.sin(x));
# np.sin makes Trigonometric sine, element-wise (sine wave)

# Make a plot from dictionary
nut_butter = {"Almond butter": 10, "Peanut butter": 8, "Cashew butter": 12}
fig, ax = plt.subplots()
# Making a bar plot
ax.bar(nut_butter.keys(), nut_butter.values());
ax.set(title="Dan's Nut Butter Store", ylabel="Price ($)");
