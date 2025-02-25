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

- What is a Queue?
    - Definition: A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
> - Common Operations:
>> - Enqueue: Add an element to the rear of the queue.
>> - Dequeue: Remove and return the front element.
>> - Peek/Front: Return the front element without removing it.
>> - isEmpty: Check if the queue is empty.

- Key Concepts:
    - FIFO (First In, First Out): The element that has been in the queue the longest is served first.
    - Efficient Operations: Python’s deque (double-ended queue) provides efficient appends and pops from both ends.

### Day 11: Linked Lists
1. Singly Linked List
- What is a Linked List?
    - Definition: A linked list is a linear data structure where each element (node) contains data and a reference (pointer) to the next node.
-Advantages:
    - Dynamic size.
    - Ease of insertion and deletion without reorganizing the entire structure.
- Disadvantages:
    - No random access (must traverse from the head to access a node).
- Components of a Linked List:
    - Node: The basic unit containing data and a pointer to the next node.
    - Head: The first node of the list.
    - Tail: The last node (optional pointer for easier insertion at the end).

- Key Concepts:
    - Node: Each node stores data and a pointer to the next node.
    - Head Pointer: Used to track the start of the linked list.
    - Traversing: To perform operations like deletion or search, you traverse the list from the head.


### Summary of Days 10-11
- Stacks & Queues:
    - Stack: LIFO structure with operations like push, pop, and peek.
    - Queue: FIFO structure with operations like enqueue, dequeue, and peek.
- Linked Lists:
    - Singly Linked List: A dynamic data structure consisting of nodes that are linked together. Learn how to append, prepend, delete, and traverse nodes.
    - Practice: Each data structure has its own set of operations. Understanding these helps in solving various real-world problems where dynamic data  management is required.

## Day 12: NumPy
### Overall Objectives
- NumPy (Day 12):
    - Understand the basics of NumPy arrays (ndarray), vectorized operations, and broadcasting.
    - Learn how to perform fast numerical computations and manipulate multi-dimensional data.
    - Gain familiarity with common functions and methods for aggregations and linear algebra.

### Day 12: Introduction to NumPy
1. Overview of NumPy
> What is NumPy?
>> - NumPy is the fundamental package for numerical computing in Python. It provides the ndarray data structure for multi-dimensional arrays, which supports efficient vectorized operations, making computations much faster than using Python lists.

- Key Features:
    - ndarray: A fast, multidimensional array object.
    - Vectorization: Operations are applied element-wise without explicit loops.
    - Broadcasting: Automatically expands arrays with different shapes for arithmetic operations.
    - Rich Functionality: Includes linear algebra, random number generation, and more.

### Day 13: Introduction to Pandas
1. Overview of Pandas
> What is Pandas?
>> - Pandas is a high-level data manipulation library built on top of NumPy. It provides two main data structures:

- Series: A one-dimensional labeled array.
- DataFrame: A two-dimensional table with labeled axes (rows and columns).
> Why Use Pandas?
>> - Pandas simplifies data cleaning, transformation, and analysis with built-in methods for merging, grouping, and summarizing data.

### Objectives for Day 14
- Understand the Role of Data Visualization:
- Learn why visualizing data is crucial for exploratory data analysis (EDA) and how it aids in uncovering trends, patterns, and outliers.

- Matplotlib Basics:
    - Create basic plots (line plots, scatter plots, bar charts, histograms, etc.).
    - Customize plots with titles, axis labels, legends, and styles.
    - Work with subplots to display multiple charts in one figure.

- Seaborn Essentials:
    - Use Seaborn’s high-level interface to generate aesthetically pleasing and informative statistical graphics.
    - Create visualizations like pair plots, heatmaps, and categorical plots to explore relationships within data.

### Section 1: Data Visualization with Matplotlib
> 1.1 Introduction to Matplotlib
>> Matplotlib is the foundational Python library for creating static, animated, and interactive visualizations. It offers fine-grained control over
every aspect of a figure, making it ideal for custom visualizations.

### Section 2: Data Visualization with Seaborn
> 2.1 Introduction to Seaborn
>> Seaborn is built on top of Matplotlib and provides a high-level interface for creating attractive statistical graphics with minimal code. It integrates  well with Pandas DataFrames and comes with several built-in themes and color palettes.

- Matplotlib: Offers extensive customization for creating various types of plots. Learn to control figure size, style, and multiple plot elements.
- Seaborn: Provides high-level abstractions for common statistical visualizations and works seamlessly with Pandas.
- Visualization Best Practices: Always label your axes, include a title and legend when appropriate, and choose color schemes that enhance clarity.

## Day 15
### Section 1: Core Concepts and Definitions
- 1.1 Scalars, Vectors, and Matrices
    - Scalar: A single number (0-dimensional), e.g., 7 or 3.14.
    - Vector: A one-dimensional array of numbers (1D). Vectors represent points or directions in space.
    - Matrix: A two-dimensional array of numbers (2D), often used to represent data sets, transformations, or coefficients in equations.
- 1.2 Vector Operations
    - Addition: Combine two vectors element-wise.
    - Scalar Multiplication: Multiply each element of a vector by a constant.
    - Dot Product: The sum of the products of corresponding entries in two vectors. This operation yields a scalar and is essential for measuring similarity or projecting one vector onto another.
    - Norm (Magnitude): A measure of the length of a vector, typically computed as the square root of the sum of the squares of its components.
- 1.3 Matrix Operations
    - Addition and Scalar Multiplication: Similar to vectors but performed element-wise over two-dimensional arrays.
    - Matrix Multiplication: Unlike element-wise multiplication, matrix multiplication involves summing the products of corresponding entries from rows and columns.
    - Transpose: Flips a matrix over its diagonal, converting rows to columns.
    - Determinant and Inverse: The determinant is a scalar value that can indicate if a matrix is invertible (a non-zero determinant means it is). The inverse of a matrix, when it exists, is the matrix that, when multiplied with the original, yields the identity matrix.

- Vector Addition and Scalar Multiplication: Performed element-wise.
- Dot Product: Computes the sum of products for corresponding elements.
- Norm: Provides the length of the vector, useful for normalization.

- Matrix Operations: Addition and multiplication are fundamental for combining data and performing linear transformations.
- Transpose: Changes the orientation of the matrix, a key operation in many algorithms.
- Determinant and Inverse: Critical for solving systems of linear equations and understanding matrix properties.

### Real-World Relevance and Additional Terms
- Why Linear Algebra?
    - Data Representation: Feature vectors and matrices represent data samples and datasets.
    - Transformations: Many machine learning models, such as linear regression and neural networks, use matrix operations to transform input data.
    - Dimensionality Reduction: Techniques like Principal Component Analysis (PCA) rely on eigenvalues and eigenvectors—a topic to explore in later sessions.
- New Terms Recap:
    - Scalar, Vector, Matrix: Basic building blocks for numerical data.
    - Dot Product & Norm: Fundamental for measuring similarity and scaling.
    - Transpose, Determinant, Inverse: Essential matrix operations that help solve equations and perform transformations.

## Day 16
- Understand Derivatives and Their Meaning:
    - Definition: Learn what a derivative is and why it represents the rate of change (slope) of a function.
    - Interpretation: Understand how derivatives indicate the direction and speed of change in a function.
- Explore Gradients and Partial Derivatives:
    - Gradient: Generalize the concept of a derivative to functions of multiple variables. The gradient is a vector of partial derivatives.
    - Application: Recognize how gradients help in optimizing cost functions in machine learning.
- Learn the Gradient Descent Optimization Algorithm:
    - Concept: Understand how gradient descent uses derivatives (gradients) to iteratively update model parameters in order to minimize a cost function.
    - Implementation: Work through a code example that demonstrates gradient descent on a simple quadratic function.
- Introduce Numerical Differentiation:
    - Finite Difference Method: See how you can approximate derivatives numerically when an analytical derivative is not available.

### Section 1: Understanding Derivatives
- 1.1 What is a Derivative?
    - Definition: The derivative of a function f(x) at a point x is the limit of the difference quotient as the increment approaches zero:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
 
- Interpretation: It represents the instantaneous rate of change or the slope of the tangent line to the function at that point.

### 1.2 Simple Example: Derivative of a Quadratic Function
For the function 
$$f(x) = x^2$$

**The analytical derivative is:**
$$f'(x) = 2x$$

- Explanation:
    - The function numerical_derivative approximates the derivative using a small increment 
    - This helps validate our understanding and can be useful when dealing with functions whose derivatives are difficult to compute analytically.

### Section 2: Gradients and Partial Derivatives
- 2.1 Extending to Multivariable Functions
**For a function** $$𝑓(𝑥,𝑦)$$
- the gradient is defined as:
$$\nabla f(x, y) = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$$

- Interpretation: The gradient vector points in the direction of the steepest ascent of the function.

### 2.2 Example: Gradient of a Simple Multivariable Function
- Consider $$𝑓(𝑥,𝑦)=𝑥2+𝑦2$$ Its gradient is: $$f(x, y) = (2𝑥,𝑦)$$

### Section 3: Gradient Descent Optimization
- 3.1 Concept of Gradient Descent
    - Goal: Minimize a cost function 
𝐽(𝜃) by iteratively updating the parameters 𝜃 in the opposite direction of the gradient.

Update Rule:
$$\theta = \theta - \alpha \nabla J(\theta)$$

**where α is the learning rate.**

**3.2 Example: Minimizing a Quadratic Function**
- Let’s minimize 𝑓(𝑥)=𝑥 2 using gradient descent. The derivative is 𝑓′(𝑥)=2𝑥

### Section 4: New Terms and Key Takeaways
- New Terms:
    - Derivative: The rate at which a function changes at any given point.
    - Gradient: A vector containing the partial derivatives with respect to each variable, indicating the direction of steepest ascent.
    - Learning Rate (𝛼): A hyperparameter that determines the step size in gradient descent.
    - Gradient Descent: An optimization algorithm that minimizes a function by iteratively moving in the direction of steepest descent (negative gradient).
- Key Takeaways:
    - Calculus in ML: Derivatives and gradients are the building blocks of many machine learning optimization algorithms.
    - Optimization: Understanding how gradient descent works is essential for tuning models such as linear regression, logistic regression, and neural networks.
    - Numerical vs. Analytical: Both analytical and numerical methods can be used to compute derivatives; each has its use depending on the situation.

### Wrap-Up
- How calculus (through derivatives and gradients) forms the core of optimization techniques in machine learning.
- Practical Application:
    - The gradient descent algorithm is not only a theoretical tool but also a practical method used in training models—its behavior (and challenges such as choosing the right learning rate) is fundamental to model tuning.
- Next Steps:
    - In upcoming sessions, you’ll continue exploring advanced topics such as probability, statistics, and more sophisticated machine learning models that build upon these calculus concepts.