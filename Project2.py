# Project 2
# Nathan Zou, July 5-17, 2023

# Eigenvalue of a square matrix
# Given non zero vectors u and w, calculate the eigenvalues and compare the 
# results of different iterations to determine which value the results converge to.

import numpy as np

# Create the square matrix A and initialize vectors u and w.
A = np.array([[3, 1], [2, 4]])
u0 = np.array([1, 1])
w = np.array([1, 0])

# Iterate to calculate u1, u2, u3, ..., u7
u = u0
results = []

for _ in range(8):
  uNext = np.dot(A, u)
  result = np.dot(w.T, uNext) / np.dot(w.T, u)
  results.append(result)
  u = uNext

# Print the results and check convergence
print("Results:")
for i, result in enumerate(results):
    print(f"n = {i+1}: {result}")

convergedValue = results[-1]
print("Converged value:", convergedValue)

# Compare (A * u_n) / ||u_n|| and (𝜆 * u_n) / ||u_n||
uNorm = np.linalg.norm(u0)

print("\nComparison for:")
for i, result in enumerate(results):
    An_u = np.dot(A, u0) / uNorm
    uEigen = result * u0 / uNorm
    print(f"n = {i+1}: (A * u_n) / ||u_n|| = {An_u}")

print("\nComparison for:")
for i, result in enumerate(results):
    uEigen = result * u0 / uNorm
    print(f"n = {i+1}: (𝜆 * u_n) / ||u_n|| = {uEigen}")