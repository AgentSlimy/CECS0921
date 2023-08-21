import math

def f(x):
    return 2 - x**2 * math.sin(x)

def bisectionMethod(a, b, tol, maxIter):
    for i in range(maxIter):
        p = (a + b) / 2
        f_p = f(p)

        if abs(f_p) < tol or abs(b - a) / 2 < tol:
            return p

        if f_p * f(a) < 0:
            b = p
        else:
            a = p

    return None

# Interval bounds
a = -1
b = 2

# Tolerance and maximum iterations
tolerance = 1e-6
maxIterations = 1000

root = bisectionMethod(a, b, tolerance, maxIterations)

if root is not None:
    print("The approximate root:", root)
else:
    print("Bisection method did not converge within the given tolerance and iterations.")
