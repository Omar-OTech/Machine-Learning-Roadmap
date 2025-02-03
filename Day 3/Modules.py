# Using a built-in module: math
import math

number = 16
# Calculate the square root using math.sqrt()
sqrt_val = math.sqrt(number)
print(f"\nThe square root of {number} is {sqrt_val}.")

print("-" * 50)

import mymath

result_add = mymath.add(10, 5)
result_subtract = mymath.subtract(10, 5)
result_multiply = mymath.multiply(10, 5)
result_divide = mymath.divide(10, 5)

print("\nCustom Module 'mymath' Results:\n")
print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)
print("Multiplication Result:", result_multiply)
print("Division Result:", result_divide)