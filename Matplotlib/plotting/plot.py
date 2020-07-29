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

# Horizantal Bar plot
fig, ax = plt.subplots()
ax.barh(list(nut_butter.keys()), list(nut_butter.values())); # For "barh" we have to turn the values into a list
ax.set(title="Dan's Nut Butter Store", xlabel="Price ($)");

# Histogram

# Make some data
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x);

# Multiple plots happening at the same time

### Two options for subplots

# Option 1
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
# This makes 4 subplots
# Plot to each different axis
ax1.plot(x, x/2);
ax2.scatter(np.random.random(10), np.random.random(10));
ax3.bar(nut_butter.keys(), nut_butter.values());
ax4.hist(np.random.randn(100));

# Option 2
