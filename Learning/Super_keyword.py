class ParentClass:
    def parent_method(self):
        print("This is a method in the ParentClass.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Hello")
        super().parent_method()
    def child_method(self):
        print("This is a method in the ChildClass.")
        super().parent_method() # Calling the parent method using super()
    
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)  # Calling the parent class constructor
        self.language = language

rai = Employee("Rai", 101)
karan = Programmer("Karan", 102, "Python")

print(karan.name)
print(karan.id)
print(karan.language)