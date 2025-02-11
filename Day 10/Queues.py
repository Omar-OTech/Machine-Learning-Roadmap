# What is a Queue?
# Definition: A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
# Common Operations:
# Enqueue: Add an element to the rear of the queue.
# Dequeue: Remove and return the front element.
# Peek/Front: Return the front element without removing it.
# isEmpty: Check if the queue is empty.

# Key Concepts:
# FIFO (First In, First Out): The element that has been in the queue the longest is served first.
# Efficient Operations: Python’s deque (double-ended queue) provides efficient appends and pops from both ends.


# Queue Implementation Example (Using Python's collections.deque)

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} -> Queue: {list(self.items)}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow! cannot dequeue from an empty queue.")
            return None
        dequeued_item = self.items.popleft()
        print(f"Dequeued {dequeued_item} -> Queue: {list(self.items)}")
        return dequeued_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.items[0]

# Testing the Queue
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Current Front:", queue.peek())
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # Test dequeuing from an empty queue