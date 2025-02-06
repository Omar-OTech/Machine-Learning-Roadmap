# Machine-Learning-Roadmap
--------------------------
## Day 1: Python Fundamentals & Basic Data Types
### Objectives:
- Understand what Python is and set up your development environment.
- Learn about variables, basic data types, and simple operations.
- Get comfortable with the interactive Python shell or a Jupyter Notebook.

>> 1. Basic Syntax & Variables:
>>> - Creating variables and assigning values.
>>> - Naming conventions and basic rules for identifiers.

>> 2. Data Types:
>>> - Numeric Types: Integers (int), Floating Point Numbers (float).
>>> - Strings: Basic string operations, concatenation, and formatting.
>>> - Booleans: True and False.
>>> - Type Checking and Casting: Using type(), int(), float(), and str() functions.

>>3. Simple Arithmetic Operations:
>>> - Addition, subtraction, multiplication, division.
>>> - Order of operations (PEMDAS).

## Day 2: Control Flow – Conditional Statements and Loops
### Objectives:
- Learn how to control the flow of your program with conditions and loops.
- Understand the use of if, elif, and else statements.
- Practice with looping constructs like for and while loops.

> Topics Covered:
>> 1. Conditional Statements:
>>> * Using if, elif, and else to execute code conditionally.
>>> * Comparison operators (==, !=, <, >, <=, >=).
>>> * Logical operators (and, or, not).

>> 2. Loops:
>>> * For Loops: Iterating over sequences (lists, strings, ranges).
>>> * While Loops: Executing a block of code repeatedly until a condition is met.
>>> * Loop Control Statements: break to exit a loop and continue to skip to the next iteration.

## Day 3: Functions and Modules
### Objectives:
- Understand the importance of functions in organizing code.
- Learn how to define and call functions.
- Explore basic modularity by creating and importing modules.

> Topics Covered:
>> 1. Functions:
>>> * Defining a function using the def keyword.
>>> * Understanding function parameters and return values.
>>> * The concept of scope (local vs. global variables).

>> 2.Modules:
>>> * What is a module and why modularity is important.
>>> * How to import standard modules (e.g., math) and use their functions.
>>> * Creating your own simple module.

## Day 4: Data Structures in Python
### Objectives:
- Understand and work with Python’s built-in data structures.
- Learn how each data structure is used, along with its advantages and limitations.
- Get acquainted with common operations and methods associated with each structure.

> ## Key Data Structures Covered:
>> 1. Lists:
>>> * Definition: An ordered, mutable (changeable) collection of items.
>>> * Usage: Ideal for maintaining a collection of items in a specific order.
>>> * Common Operations: Indexing, slicing, appending, inserting, removing, and iterating.

>> 2. Tuples:
>>> * Definition: An ordered, immutable collection of items.
>>> * Usage: Useful for storing data that should not change after creation (e.g., coordinates, fixed configurations).
>>> * Common Operations: Indexing, slicing, and unpacking.

>> 2. Dictionaries:
>>> * Definition: An unordered collection of key-value pairs. Keys must be unique and immutable (usually strings, numbers, or tuples), while values can be any type.
>>> * Usage: Excellent for fast lookup, insertion, and deletion of items by keys.
>>> * Common Operations: Accessing values by keys, adding new key-value pairs, updating values, and iterating over keys/values.

>> 3. Sets:
>>> * Definition: An unordered collection of unique items.
>>> * Usage: Ideal for membership testing, removing duplicates, and performing mathematical set operations (union, intersection, difference).
>>> * Common Operations: Adding items, removing items, and set operations.

> ## New Terms Explained:
>> ### Mutable vs. Immutable:
>>> * Mutable: Objects that can be changed after they are created (e.g., lists, dictionaries, sets, etc...).
>>> * Immutable: Objects that cannot be changed once created (e.g., tuples, strings, float, int, unicode, bool, etc...).
>> - Indexing: Accessing elements of a sequence (list, tuple) using an index. Indexes start at 0.
>> - Slicing: Extracting a part of a sequence by specifying a start and end index.
>> - Key-Value Pair: In dictionaries, each key is associated with a value. Keys are unique identifiers.
>> - Set Operations: Mathematical operations on sets such as union (combining items), intersection (common items), and difference (items in one set but not the other).

## Day 5: Introduction to Basic Algorithms
### Objectives:
- Understand what an algorithm is and why efficient algorithms are important.
- Learn basic algorithmic concepts including searching and sorting.
- Implement simple examples to see these concepts in action.

> ## Key Concepts Covered:
>> 1. Algorithm:
>>> * Definition: A finite sequence of well-defined instructions for solving a problem or performing a computation.
>>> * Importance: Efficient algorithms save time and resources, which is crucial for processing large datasets.

>> 2. Searching Algorithms:
>>> * Linear Search: A simple method of finding an element by checking each item in a list sequentially.
>>> * Binary Search: An efficient algorithm for finding an item in a sorted list by repeatedly dividing the search interval in half.

>> 3. Sorting Algorithms:
>>> * Definition: Methods for arranging data in a particular order (ascending or descending).
>>> * Example – Bubble Sort: A simple (but not very efficient) sorting algorithm that repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order.


> ## New Terms Explained:
>> - Algorithm Efficiency: A measure of the amount of time and/or space an algorithm requires as a function of the size of the input data.
>> - Time Complexity: Often expressed using Big O notation (e.g., O(n) for linear search, O(log n) for binary search), it describes how the running time increases with the input size.
>> - Linear Search: Checks each element one-by-one until the target is found. It is simple but has a time complexity of O(n).
>> - Binary Search: Efficiently finds an element in a sorted list by repeatedly dividing the list. Its time complexity is O(log n).
>> - Bubble Sort: A straightforward comparison-based sorting algorithm where each pair of adjacent elements is compared and swapped if necessary. It has a worst-case time complexity of O(n²), making it less efficient for large lists.

## Day 6: Recursion & Sorting Algorithms
### 1. Recursion
> What is Recursion?
>> - Recursion is when a function calls itself to solve a smaller instance of the same problem. It continues until a base case is met.

### Key Concepts:
- Base Case: The condition where recursion stops.
- Recursive Case: The function calls itself with a smaller input.
- Stack Overflow: If no base case is defined, recursion continues indefinitely and causes a memory overflow.
- Example: Factorial using 

### Factorial of n is defined as

#### $${ (n)!=(n)×(n−1)! }$$ where 1!=1

```python
def factorial(n):
    if n == 1: # base case
        return 1
    return n * factorial(n-1) # recursive case

print(factorial(5)) # 120
print(factorial(10)) #3628800
```
### Example: Fibonacci using Recursion
#### The Fibonacci sequence is defined as:

#### $${ F(n)=F(n−1)+F(n−2) }$$
#### where $${ 𝐹(0)=0,𝐹(1)=1F(0)=0,F(1)=1 }$$

```python
def fibonacci(n):
    if n <= 1:
        return n  # Base cases: F(0) = 0, F(1) = 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print(fibonacci(6))  # Output: 8
```

## 2. Sorting Algorithms
- Sorting is the process of arranging elements in ascending or descending order. There are many sorting techniques, each with different efficiency levels.
> Bubble Sort (Simple but Inefficient)
>> Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.

## Merge Sort (Efficient)
- Merge Sort is a divide and conquer algorithm that splits the list into halves, sorts them, and merges them back.

## Day 7: Quick Sort & File Handling
> 1. Quick Sort
>> - Quick Sort is another divide and conquer sorting algorithm that selects a pivot, partitions the array, and recursively sorts the partitions.

## Quick Sort Algorithm
- Select a pivot (typically the last element).
- Partition the array such that elements smaller than the pivot go to the left and greater ones go to the right.
- Recursively apply Quick Sort on the partitions.

## 2. File Handling in Python
File handling allows us to store and manipulate data in files instead of in-memory lists or dictionaries.

### Opening & Writing to a File
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python File Handling.")
```



| Mode  |                 Description               |
|-------|-------------------------------------------|
| r     | Read mode (default)                       |
| w     | Write mode (overwrites the file)          |
| a     | Append mode (adds content at the end)     |
| r+    | Read and write mode                       |
| w+    | Write and read mode (overwrites the file) |

### Recursion: Functions that call themselves, solving smaller versions of the same problem.
> Sorting Algorithms:
>> - Bubble Sort (slow)
>> - Merge Sort (fast, divide & conquer)
>> - Quick Sort (fast, uses a pivot)

## Days 8-9: Object-Oriented Programming (OOP) in Python
### Objectives for Days 8-9
- Learn about Object-Oriented Programming (OOP) principles.
- Understand and implement Classes, Objects, Encapsulation, Inheritance, and Polymorphism.
- Apply OOP concepts in real-world scenarios with practical examples.

### Day 8: Introduction to OOP & Classes
1. What is Object-Oriented Programming (OOP)?
>> OOP is a programming paradigm that organizes code into reusable objects, making it more modular, scalable, and efficient.

2. Key Concepts in OOP

| Concept       |                 Description                               |
|---------------|-----------------------------------------------------------|
| Class         | A blueprint/template for creating objects.                |
| Object        | An instance of a class with unique data.                  |
| Encapsulation | Restricting direct access to some of an object's data.    |
| Inheritance   | Creating new classes from existing ones (code reuse).     |
| Polymorphism  | Using the same method name for different behaviors.       |

3. Defining a Class & Creating an Object
- Example: Creating a Car Class

```python
class Car:
    def __init__(self, brand, model, year):  # Constructor
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating Objects (Instances)
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.display_info())  # Output: 2022 Toyota Corolla
print(car2.display_info())  # Output: 2023 Honda Civic
```

### Explanation
- __init__ is the constructor method that initializes object attributes.
- self represents the instance of the class.
- Methods (like display_info) define behavior for the objects.

4. Encapsulation (Data Hiding)
- Encapsulation restricts direct access to object data and protects it from unintended modifications.
Example: Private Attributes
```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute (double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def get_balance(self):
        return f"Balance: ${self.__balance}"

# Creating Object
account = BankAccount("John Doe", 1000)

account.deposit(500)
print(account.get_balance())  # Output: Balance: $1500

# Accessing Private Attribute (Throws an error)
# print(account.__balance)  # AttributeError
```
> Explanation
>> - __balance is private (cannot be accessed outside the class).
>> - The get_balance method is used to retrieve the balance safely.

### Day 9: Inheritance & Polymorphism
1. Inheritance (Code Reuse)
- Inheritance allows a class to derive properties from another class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"

# Derived Class
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Derived Class
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating Objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, ":", dog.speak())  # Output: Buddy : Woof! Woof!
print(cat.name, ":", cat.speak())  # Output: Whiskers : Meow!
```

2. Polymorphism (Same Function, Different Behavior)
- Polymorphism allows different classes to use the same method name but behave differently.

```python
class Bird:
    def fly(self):
        return "Bird can fly"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies at low altitude"

class Eagle(Bird):
    def fly(self):
        return "Eagle flies at high altitude"

# Function demonstrating Polymorphism
def flying_test(bird):
    print(bird.fly())

sparrow = Sparrow()
eagle = Eagle()

flying_test(sparrow)  # Output: Sparrow flies at low altitude
flying_test(eagle)    # Output: Eagle flies at high altitude
```

### Summary of Days 8-9
> OOP Concepts:
>> - Classes & Objects: Creating reusable templates for objects.
>> - Encapsulation: Restricting access to private attributes.
>> - Inheritance: Creating new classes from existing ones.
>> - Polymorphism: Using the same method in different ways.
- Multiple Inheritance: A class inheriting from multiple parent classes.

## Days 10–11: Advanced Data Structures – Stacks, Queues, and Linked Lists
### Learning Objectives
- Understand Specialized Data Structures: Learn the characteristics, use cases, and operations for stacks, queues, and linked lists.
- Implement Custom Data Structures: Write Python classes to simulate these data structures from scratch.
- Analyze Operations: Understand the time complexity of common operations (e.g., push/pop, enqueue/dequeue, insertion/deletion).

Day 10: Stacks & Queues
1. Stacks
- What is a Stack?
    - Definition: A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
> - Common Operations:
>> - Push: Add an element to the top of the stack.
>> - Pop: Remove and return the top element.
>> - Peek/Top: Return the top element without removing it.
>> - isEmpty: Check if the stack is empty.

- LIFO (Last In, First Out): The most recently added element is the first one to be removed.
- Dynamic Size: Unlike static arrays, stacks implemented with Python lists can grow as needed.