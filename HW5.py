import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# a)
def lagrange_basis(i, x, xValues):
    basis = 1.0
    for j, xj in enumerate(xValues):
        if i != j:
            basis *= (x - xj) / (xValues[i] - xj)
    return basis

def lagrange_interpolation(x, xValues, yValues):
    result = 0.0
    for i, yi in enumerate(yValues):
        result += yi * lagrange_basis(i, x, xValues)
    return result

xValues = np.array([0.5, 0.7, 1.0])
yValues = np.array([x**3 - np.exp(-x) for x in xValues])

x = 0.8
P2x = lagrange_interpolation(x, xValues, yValues)
print("P2(0.8):", P2x)

# b)
fx = x**3 - np.exp(-x)
error = abs(fx - P2x)
print("Actual error:", error)

# c)
# Create interpolation function
interpolationFunction = interp1d(xValues, yValues, kind = 'quadratic')

# Generate x values for plotting
xPlot = np.arange(0.5, 1.0, 0.1)

# Evaluate interpolation function at the xPlot values
yInterpolated = interpolationFunction(xPlot)

# Plotting
plt.figure()
plt.plot(xValues, yValues, 'o', label = 'Data Points')
plt.plot(xPlot, yInterpolated, '--', label = 'Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolation using SciPy')
plt.legend()
plt.show()