class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"Vehicle: {self.brand} - {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type
    
    def display_info(self):
        return f"Bike: {self.brand} - {self.model} - Type: {self.bike_type}"

# Example usage
car = Car("Toyota", "Corolla", 4)
bike = Bike("Harley-Davidson", "Street 750", "Cruiser")

print(car.display_info())  # Output: Car: Toyota Corolla, Doors: 4
print(bike.display_info())  # Output: Bike: Harley-Davidson - Street 750 - Type: Cruiser