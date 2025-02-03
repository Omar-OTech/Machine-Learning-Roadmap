# 1. Variables and Data Types
# Define an integer variable

age = 30
print("\nAge:", age, "| Type:", type(age))

print("-" * 50)

# Define a floating point variable
price = 19.99
print("Price:", price, "| Type:", type(price))

print("-" * 50)

# Define a string variable
greeting = "Hello, ML World!"
print("Greeting:", greeting, "| Type:", type(greeting))

print("-" * 50)

# Define a boolean variable
is_ml_awesome = True
print("Is ML Awesome?", is_ml_awesome, "| Type:", type(is_ml_awesome))

print("-" * 50)

# 2. Basic Arithmetic Operations
a = 10
b = 5
print("\nArithmetic Operations:")
print(f"Addition ({a} + {b}):", a + b)
print(f"Subtraction ({a} - {b}):", a - b)
print(f"Multiplication ({a} * {b}):", a * b)
print(f"Division ({a} / {b}):", a / b)
print(f"Integer Division ({a} // {b}):", a // b)
print(f"Modulus ({a} % {b}):", a % b)

print("-" * 50)
# 3. String Operations
# Concatenation
first_name = 'Ali'
last_Name = 'Ahmed'
full_name = first_name + ' ' + last_Name
print("\nString Operations:", full_name)

print("-" * 50)

# String Formatting
age_info = f"{full_name} is {age} years old."
print(age_info)

print("-" * 50)

# 4. Type Conversion (Casting)
num_str = '100'
num_int = int(num_str)
print("Converted '100' (str) to:", num_int, "| Type:", type(num_int))