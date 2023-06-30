# Project 1 
# Nathan Zou, June 28-30, 2023

# Problem 1. Surface Area and Volume of a Sphere
# Given a user inputted radius, calculate the surface area and volume of a sphere using equations.

import math

print("Problem 1. Surface Area and Volume of a Sphere", "\n")

# User inputted radius
radius = float(input("Enter the radius of the sphere: "))

# Calculations for surface area and volume
surfaceArea = 4 * math.pi * radius**2
volume = (4/3) * math.pi * radius**3

# Round surface area and volume to 1 decimal place
surfaceArea = round(surfaceArea, 1)
volume = round(volume, 2)

# Print results with formatted output
print(f"{radius:.4f} is the value of the radius.")
print(f"In a sphere of radius {radius:.4f}, the surface area is {surfaceArea:.1f}.")
print(f"And its volume is {volume:.2E}.", "\n\n")


# Problem 2. Fibonacci Numbers
# Using the Fibonacci Sequence, find the minimum Fibonacci number that is greater than 4000 
# and find the number of Fibonacci numbers that are less than 5000.

print("Problem 2. Fibonacci Numbers", "\n")

# Create Fibonacci Sequence
def fibonacciSequence():
    fibNum = [0, 1] # Start sequence with the first two numbers, 0 and 1
    while True:
        nextNum = fibNum[-1] + fibNum[-2] # Generate the following numbers by adding the previous two together
        if nextNum > 5000: # Stop loop if the next number exceeds 5000
            break
        fibNum.append(nextNum) # Add the number to sequence
    return fibNum

def findMinGreater4000(sequence):
    for number in sequence:
        if number > 4000: # Find the first number in the previously generated sequence that is greater than 4000
            return number

def countLess5000(sequence):
    count = 0
    for number in sequence:
        if number < 5000: # Count the number of Fibonaaci numbers that are less than 5000
            count += 1
        else:
            break
    return count

fibSequence = fibonacciSequence() 
minGreater4000 = findMinGreater4000(fibSequence)
countLess5000 = countLess5000(fibSequence)

# Print results
print("Fibonacci sequence:")
print(fibSequence)

print("\nMinimum Fibonacci number greater than 4000:")
print(minGreater4000)

print("\nNumber of Fibonacci numbers less than 5000:")
print(countLess5000)