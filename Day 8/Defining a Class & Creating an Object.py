class Car:
    def __init__(self, brand, model, year):   # Constructor
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} - {self.brand} - {self.model}"

# Creating Objects (Instances)
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.display_info())  # Output: 2022 Toyota Corolla
print(car2.display_info())  # Output: 2023 Honda Civic


# __init__ is the constructor method that initializes object attributes.
# self represents the instance of the class.
# Methods (like display_info) define behavior for the objects.