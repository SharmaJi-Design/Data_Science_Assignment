import random
random.seed(4090)

# Generate random data
data = [random.randint(30, 100) for i in range(50)]

# Function to calculate mode
def mode(data):
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    # Sort by frequency descending
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[0][0]

# Function to calculate mean
def mean(data):
    return sum(data)/len(data)

# Function to calculate median
def median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n//2 - 1] + data[n//2])/2
    else:
        return data[n//2]

# Function to calculate quartiles
def quartile(data, n):
    data.sort()
    l = len(data)
    q_term = (l - 1) * n / 4
    term = int(q_term)
    dec = q_term - term

    if dec != 0:
        q = data[term] + dec * (data[term + 1] - data[term])
    else:
        q = data[term]
    return q

# Calculations
mean_value = mean(data)
median_value = median(data)
mode_value = mode(data)
data_range = max(data) - min(data)
q1 = quartile(data, 1)
q2 = quartile(data, 2)
q3 = quartile(data, 3)
iqr = q3 - q1

# Print results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Range: {data_range}")
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
