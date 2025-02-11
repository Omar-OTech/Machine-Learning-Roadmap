# LIFO (Last In, First Out): The most recently added element is the first one to be removed.
# Dynamic Size: Unlike static arrays, stacks implemented with Python lists can grow as needed.

# What is a Stack?
# Definition: A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
# Common Operations:
# Push: Add an element to the top of the stack.
# Pop: Remove and return the top element.
# Peek/Top: Return the top element without removing it.
# isEmpty: Check if the stack is empty.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} -> Stack: {self.items}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        popped_item = self.items.pop()
        print(f"Popped {popped_item} -> Stack: {self.items}")
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.items[-1]

# Test the Stack class
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Current Top:", stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.pop()