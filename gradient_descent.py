import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("content\\linear_dataset.csv", sep=',', header=None)
X = dataset.iloc[:, 0]
Y = dataset.iloc[:, 1]

total_values = len(X)

slope, const = 0, 0
learning_rate = 0.0001

for epoch in range(1000):
    Y_pred = slope * X + const

    diff_slope = (-2 / total_values) * sum(X * (Y - Y_pred))
    diff_const = (-2 / total_values) * sum(Y - Y_pred)

    slope = slope - (learning_rate * diff_slope)
    const = const - (learning_rate * diff_const)

print("Slope: ", slope)
print("Intercept: ", const)

max_value = np.max(X)
min_value = np.min(X)
split_values = np.linspace(min_value, max_value, 100)

new_line = const + slope * split_values

plt.plot(split_values, new_line, color="BLUE", label="Regression Line")
plt.scatter(X, Y, color="RED", label="Scatter points")
plt.xlabel("Independent variable")
plt.ylabel("Dependent variable")
plt.legend()
plt.show()

# Predicting the values of y
Y_pred = const + slope * X

mean_squared_error = sum((Y - Y_pred) ** 2) / total_values
root_mean_squared_error = np.sqrt(mean_squared_error)
print("Mean squared error: ", mean_squared_error)
print("Root mean squared error: ", root_mean_squared_error)

ssr = sum((Y - Y_pred) ** 2)
sst = sum((Y - np.mean(Y)) ** 2)
r2_score = 1 - (ssr / sst)
print("Square of residuals: ", ssr)
print("Sum of squares: ", sst)
print("R2 score or coefficient of determination: ", r2_score)
