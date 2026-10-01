import numpy as np

# 1. Create a 1D array containing numbers from 1 to 10
arr = np.arange(1, 11)
print("Original array:", arr)

# 2. Slicing operations
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])

# 3. Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting
# Add 5 to every element
arr = arr + 5
print("After adding 5:", arr)

# Multiply every element by 2
arr = arr * 2
print("After multiplying by 2:", arr)
