def fibonacci(n):
    if n <= 1:
        return n  # Base cases: F(0) = 0, F(1) = 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
    
print(fibonacci(6)) # 8