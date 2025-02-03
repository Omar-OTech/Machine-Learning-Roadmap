# Define a simple function to calculate the square of a number
def square(number):
    return number * number

# Define a function to greet a user by name
def greet(name):
    """Greet the user with their name."""
    return f"\nHello, {name}! Welcome to Machine learning Journey."

# Using the functions
num = 7
print(f"\nThe square of {num} is {square(num)}.")

print("-" * 50)

user = "Alice"
print(greet(user))

print("-" * 50)

# Demonstrating local vs. global scope
global_var = "I am global"

def check_scope():
    local_var = "I am local"
    print(f"Local variable: {local_var} (accessed from inside function)")
    print(f"Global variable: {global_var} (accessed from inside function)")

check_scope()
# print("Local variable:", local_var) # This will raise an error
print("Outside function:", global_var)