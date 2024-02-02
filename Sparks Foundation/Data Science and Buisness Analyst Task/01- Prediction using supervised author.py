# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
url = "http://bit.ly/w-data"
data = pd.read_csv(url)

# Explore the first few rows of the dataset
print(data.head())

# Visualize the data using a scatter plot
plt.scatter(data["Hours"], data["Scores"])
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Study Hours vs. Scores")
plt.show()

# Split the data into training and testing sets
X = data[["Hours"]]
y = data["Scores"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the score for 9.25 hours of study
hours_to_predict = np.array([[9.25]])
predicted_score = model.predict(hours_to_predict)[0]
print(f"Predicted score for 9.25 hours of study: {predicted_score:.2f}%")
