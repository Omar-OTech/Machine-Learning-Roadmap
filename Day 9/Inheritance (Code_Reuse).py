# Inheritance (Code Reuse)
# Inheritance allows a class to derive properties from another class.

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Animal makes a sound."
    
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"
        
# Creating Objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, ":", dog.speak())  # Output: Buddy : Woof! Woof!
print(cat.name, ":", cat.speak())  # Output: Whiskers : Meow!