# Multiple Inheritance
# A class can inherit from multiple parent classes.

class A:
    def method_A(self):
        return "Method from Class A"

class B:
    def method_B(self):
        return "Method from Class B"

class C(A, B):
    def method_C(self):
        return "Method from Class C"

obj = C()
print(obj.method_A())  # Output: Method from Class A
print(obj.method_B())  # Output: Method from Class B
print(obj.method_C())  # Output: Method from Class C