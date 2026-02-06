# 1. Train linear regression on a dataset. Show where it fails. Apply polynomial
# regression and compare results using plots. Write a short explanation.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 1. Create a non-linear dataset
np.random.seed(42)
X = np.linspace(-3, 3, 50).reshape(-1, 1)
y = X**2 + np.random.randn(50, 1)

# 2. Train Linear Regression
linear_model = LinearRegression()
linear_model.fit(X, y)
y_linear_pred = linear_model.predict(X)

# 3. Train Polynomial Regression (degree = 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_poly_pred = poly_model.predict(X_poly)

# 4. Plot Linear Regression result (failure case)
plt.figure()
plt.scatter(X, y)
plt.plot(X, y_linear_pred)
plt.title("Linear Regression on Non-Linear Data")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# 5. Plot Polynomial Regression result (better fit)
plt.figure()
plt.scatter(X, y)
plt.plot(X, y_poly_pred)
plt.title("Polynomial Regression (Degree 2)")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Linear regression fails when the relationship between variables is non-linear because it can only
# learn straight-line patterns. In the given dataset, the data follows a quadratic curve, so the 
# linear model underfits and produces large errors. Polynomial regression solves this problem by 
# adding higher-order terms (such as 𝑥 square), allowing the model to learn curved relationships 
# fit the data more accurately.