# Base class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Derived class: Employee
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
person = Person("Alice", 25)
employee = Employee("Bob", 30, 50000)

print(person.display_info())  # Output: Name: Alice, Age: 25
print(employee.display_info())  # Output: Employee: Bob, Age: 30, Salary: 50000