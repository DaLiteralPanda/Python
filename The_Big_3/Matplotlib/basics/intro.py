import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

# Making a Plot
plt.plot()
# Getting rid of the empty brackets
plt.plot();
# If we didnt want the semicolon
plt.plot()
plt.show()

# Making some thing in the blank (canvas ig)
plt.plot([1,2,3,4]);

x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
plt.plot(x, y);

# 1st method
fig = plt.figure() # Create a figure
ax = fig.add_subplot() # Adds some axes
plt.show()

# Second Method
fig = plt.figure() # Creates a figure
ax = fig.add_axes([1,1,1,1]) # Add axes to the figure
ax.plot(x, y) # Add some data
plt.show()

# 3rd Method (recommended)
fig, ax = plt.subplots()
ax.plot(x, [50, 100, 200, 250]); # Adds some data
type(fig), type(ax)

#####
# Matplotlib example workflow
#####

# 0. Import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt

# 1. Prepare data
x = [1, 2, 3, 4]
y = [11, 12, 33, 45]

# 2. Setup Plot
fig, ax = plt.subplots(figsize=(5, 5)) # width, height

# 3. Plot the data
ax.plot(x, y)

# 4. Customise plot
ax.set(title="Simple Plot", xlabel="x-axis", ylabel="y-axis")

# 5. Save & show (the whole figure)
fig.savefig("./img/sample-plot.png")
