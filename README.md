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