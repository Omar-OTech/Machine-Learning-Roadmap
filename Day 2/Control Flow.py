# 1. Conditional Statements
number = 15

if number < 10:
    print("The number is less than 10.")
elif 10 <= number < 20:
    print("The number is between 10 and 19.")
else:
    print("The number is 20 or greater.")

print("-" * 50)

# Using logical operators
temperature = 25 # Celsius
if temperature > 20 and temperature < 30:
    print("The weather is pleasant.")

print("-" * 50)

# 2. For Loop: Iterating over a list
fruits = ['apple', 'banana', 'cherry']
print("\nFruits List:")
for fruit in fruits:
    print(fruit.capitalize())

print("-" * 50)

# For Loop: Using range()
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i, end=' ')
print()   # For new line

print("-" * 50)

print("\nCountdown:")
count = 5
while count > 0:
    print(count, end=' ')
    count -= 1  # Decrement the count
print("Blast off!")

print("-" * 50)

# 4. Loop Control: Using break and continue
print("\nLoop with break and continue:")
for num in range(1, 11):
    if num == 5:
        print("Skipping number 5 using continue.")
        continue  # Skip the rest of the loop when num is 5
    elif num == 8:
        print("Breaking out of loop at 8.")
        break   # Exit loop when num is 8
    print(num)
    