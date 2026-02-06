# 2. Train logistic regression on a binary dataset. Plot decision boundary. Show
# predicted probabilities. Explain why logistic regression is suitable for
# classification.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# 1. Create binary classification dataset
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=42
)

# 2. Train Logistic Regression
model = LogisticRegression()
model.fit(X, y)

# 3. Create grid for decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)

# 4. Predict probabilities on grid
grid_points = np.c_[xx.ravel(), yy.ravel()]
probs = model.predict_proba(grid_points)[:, 1]
Z = probs.reshape(xx.shape)

# 5. Plot decision boundary
plt.figure()
plt.contourf(xx, yy, Z, alpha=0.5)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# 6. Plot predicted probabilities
sample_probs = model.predict_proba(X)[:, 1]

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=sample_probs)
plt.title("Predicted Probabilities (Class = 1)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
