# Factorial of n is defined as:
# n!=n×(n−1)!where 1!=1
# Recursion is when a function calls itself to solve a smaller instance of the same problem. It continues until a base case is met.
def factorial(n):
    if n == 1: # base case
        return 1
    return n * factorial(n-1) # recursive case

print(factorial(5)) # 120
print(factorial(10)) #3628800