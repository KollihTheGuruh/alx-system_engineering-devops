# !/bin/bash

import numpy as np

# Experimental Data
data = [
    [61.2, 3, 1, 0, 0, 0, 0, 0],
    [36.2, 0, 0, 9, 3, 3, 2, 3],
    [175.0, 1, 1, 0, 0, 0, 0, 0],
    [-7.75, 0, 0, 1, 1, 1, 2, 1],
    [-7.77, 0, 0, 2, 2, 0, 0, 0],
    [-729, 2, 0, 0, 0, 0, 0, 0],
    [76.1, 0, 0, 2, 0, 2, 0, 0],
    [31.9, 0, 0, 4, 0, 0, 0, 2],
    [769, 1, 1, 0, 0, 0, 0, 0],
    [-54.2, 0, 0, 1, 1, 1, 2, 1],
    [41.7, 0, 0, 2, 2, 0, 0, 0],
    [123, 0, 0, 2, 0, 2, 0, 0]
]

# Extract data
Z = np.array([row[0] for row in data])
A = np.array([row[1:] for row in data])

# Calculate the matrix (A^T * A)
ATA = np.dot(A.T, A)

# Calculate the right-hand side (A^T * Z)
ATZ = np.dot(A.T, Z)

# Solve the normal equations using the least squares method
try:
  coefficients = np.linalg.solve(ATA, ATZ)
except np.linalg.LinAlgError:
  raise ValueError("The 'coefficients' variable does not contain 8 values.")

# The 'coefficients' variable now contains the eight material constants a, b, c, d, e, f, g, and h
a, b, c, d, e, f, g, h = coefficients

# Print the results
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)
print("g:", g)
print("h:", h)
