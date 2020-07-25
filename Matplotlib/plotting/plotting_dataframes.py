import pandas as pd
%matplotlib inline
# Dark Background
# plt.style.use('dark_background')
import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Making a Data Frame

df = pd.DataFrame()

df['x'] = random.sample(range(1, 100), 25)
df['y'] = random.sample(range(1, 100), 25)

df.head()

# Scatterplot
sns.lmplot('x', 'y', data=df, fit_reg=False)

# Density Plot
sns.kdeplot(df.y)
sns.kdeplot(df.y, df.x)
sns.distplot(df.x)
# Histogram
plt.hist(df.x, alpha=.3)
sns.rugplot(df.x);

car_sales = pd.read_csv("../data/car-sales.csv")

car_sales.head()

plt.hist(car_sales["Doors"])

sns.barplot(x=car_sales.index, y=car_sales.Doors, data=car_sales)

h
