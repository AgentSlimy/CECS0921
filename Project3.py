# Project 3
# Nathan Zou, July 24-28, 2023

# Finding the solution of a provided equation using Bisection, Newton's, and Secant method
# then taking those values and plotting using MatPlotLib to visualize the results.

import numpy as np
import matplotlib.pyplot as plt

# Define the equation: sin(x) - e^(-x) = 0
def equation(x):
  return np.sin(x) - np.exp(-x)

# Bisection method
def bisectionMethod(a, b, tol = 0.00001, maxIterations = 100):
  iterations = 0
  approximations = []
    
  while abs(b - a) > tol and iterations < maxIterations:
    c = (a + b) / 2
    approximations.append(c)
        
    if equation(c) == 0:
      break
    elif equation(a) * equation(c) < 0:
      b = c
    else:
      a = c
    iterations += 1
    
  if iterations < maxIterations:
    approximations.append(c)
        
  return c, approximations

# Newton's method
def newtonMethod(x0, tol = 0.00001, maxIterations = 100):
  iterations = 0
  approximations = []
    
  while iterations < maxIterations:
    x1 = x0 - equation(x0) / (np.cos(x0) + np.exp(-x0))
    approximations.append(x1)
        
    if abs(x1 - x0) < tol:
      break
        
    x0 = x1
    iterations += 1
    
  if iterations < maxIterations:
    approximations.append(x1)
        
  return x1, approximations

# Secant method
def secantMethod(x0, x1, tol = 0.00001, maxIterations = 100):
  iterations = 0
  approximations = []
    
  while iterations < maxIterations:
    x2 = x1 - equation(x1) * (x1 - x0) / (equation(x1) - equation(x0))
    approximations.append(x2)
        
    if abs(x2 - x1) < tol:
      break
        
    x0 = x1
    x1 = x2
    iterations += 1
    
  if iterations < maxIterations:
    approximations.append(x2)
        
  return x2, approximations

# Set up on interval: [0, π/2]
a, b = 0, np.pi / 2

# Initial guess for Newton's and Secant methods
x0_newton = np.pi / 4
x0_secant = np.pi / 3
x1_secant = np.pi / 4

# Find solutions, convergence, and plot for each method 
tolerance = 0.0001
bisectionSolution, bisectionConvergence = bisectionMethod(a, b, tol = tolerance)
newtonSolution, newtonConvergence = newtonMethod(x0_newton, tol = tolerance)
secantSolution, secantConvergence = secantMethod(x0_secant, x1_secant, tol = tolerance)
bisectionIterations = np.arange(1, len(bisectionConvergence) + 1)
newtonIterations = np.arange(1, len(newtonConvergence) + 1)
secantIterations = np.arange(1, len(secantConvergence) + 1)

plt.plot(bisectionIterations, bisectionConvergence, label = 'Bisection Method')
plt.plot(newtonIterations, newtonConvergence, label = "Newton's Method")
plt.plot(secantIterations, secantConvergence, label = 'Secant Method')
plt.axhline(y = bisectionSolution, color = 'b', linestyle = '--', label = 'Bisection Solution')
plt.axhline(y = newtonSolution, color = 'g', linestyle = '--', label = "Newton's Solution")
plt.axhline(y = secantSolution, color = 'r', linestyle = '--', label = 'Secant Solution')
plt.xlabel('Iterations')
plt.ylabel('Approximation')
plt.title('Convergence of Numerical Methods')
plt.legend()
plt.grid(True)
plt.show()