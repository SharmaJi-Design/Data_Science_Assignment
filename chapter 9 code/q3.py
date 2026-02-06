# 3. Train multi-class logistic regression on the Iris dataset. Report accuracy and
# confusion matrix. Visualize prediction confidence. Explain model performance.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Iris dataset
iris = load_iris()
X = iris.data[:, :2]   # first two features
y = iris.target

# Train Logistic Regression (NO multi_class argument)
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Predictions
y_pred = model.predict(X)
y_prob = model.predict_proba(X)

# Accuracy
accuracy = accuracy_score(y, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
print("Confusion Matrix:\n", cm)

# Plot confusion matrix
plt.figure()
plt.imshow(cm)
plt.colorbar()
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

# Prediction confidence (max probability)
confidence = np.max(y_prob, axis=1)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=confidence)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Prediction Confidence (Max Probability)")
plt.show()
