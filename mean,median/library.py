import random
import numpy as np

random.seed(4090)

# Generate random data
data = np.array([random.randint(30, 100) for i in range(50)])

# Mean and Median
mean = np.mean(data)
median = np.median(data)

# Mode
unique, count = np.unique(data, return_counts=True)
mode = unique[count.argmax()] 

# Range
data_range = np.ptp(data) 

# Quartiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Print results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Range: {data_range}")
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
