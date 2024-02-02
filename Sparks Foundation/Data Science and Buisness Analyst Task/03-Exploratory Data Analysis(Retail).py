# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
superstore = pd.read_csv('https://bit.ly/3i4rbWl')

# Preview first 5 rows
superstore.head()

# Preview last 5 rows
superstore.tail()

# Preview info
superstore.info

# Preview detail
superstore.describe

# Preview columns
superstore.columns()

