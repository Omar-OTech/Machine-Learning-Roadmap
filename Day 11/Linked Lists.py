# Key Concepts:
# Node: Each node stores data and a pointer to the next node.
# Head Pointer: Used to track the start of the linked list.
# Traversing: To perform operations like deletion or search, you traverse the list from the head.


# Linked Lists
# 1. Singly Linked List
# What is a Linked List?
# Definition: A linked list is a linear data structure where each element (node) contains data and a reference (pointer) to the next node.
# Advantages:
# Dynamic size.
# Ease of insertion and deletion without reorganizing the entire structure.
# Disadvantages:
# No random access (must traverse from the head to access a node).
# Components of a Linked List:
# Node: The basic unit containing data and a pointer to the next node.
# Head: The first node of the list.
# Tail: The last node (optional pointer for easier insertion at the end).


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Add a node with the specified data at the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            print(f"Appended {data} as head -> Linked List: {self}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Appended {data} -> Linked List: {self}")

    def prepend(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Prepended {data} -> Linked List: {self}")

    def delete(self, key):
        """Delete the first occurrence of key in the list."""
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            print(f"{key} not found in the list.")
            return
        if previous is None:
            # The node to be deleted is the head
            self.head = current.next
        else:
            previous.next = current.next
        print(f"Deleted {key} -> Linked List: {self}")

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "Empty List"

# Testing the Linked List
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
print("Current List:", ll)
ll.delete(20)
ll.delete(5)
ll.delete(100)  # Attempt to delete a non-existent element
