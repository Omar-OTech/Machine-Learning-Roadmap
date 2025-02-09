# The fly method is defined in all classes but behaves differently.
# flying_test(bird) works with any object that has a fly method (polymorphism).

class Bird:
    def fly(self):
        return "Bird flies."

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies at low altitude"

class Eagle(Bird):
    def fly(self):
        return "Eagle flies at high altitude"

def flying_test(bird):
    print(bird.fly())

sparrow = Sparrow()
eagle = Eagle()

flying_test(sparrow)  # Output: Sparrow flies at low altitude
flying_test(eagle)    # Output: Eagle flies at high altitude