# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The name of employee {self.id} is {self.name}")

# class Programmer(Employee):   #Inheritance, Programmer class is inheriting Employee class
#     def showLanguage(self):
#         print("the default language is Python")
# e1 = Employee("Priya", 100)
# e1.showDetails()

# e2 = Programmer("Ronit", 101)
# e2.showDetails()
# e2.showLanguage()

# # Single inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Bark!")

# d = Dog("Dog", "Doggerman")
# d.make_sound()

# a = Animal("Dog", "Dog")
# a.make_sound()


# # Multiple inheritance
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"The name of employee is {self.name}")


# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance

#     def show(self):
#         print(f"The dance of employee is {self.dance}")


# class DancerEmployee(Employee, Dancer):
#     def __init__(self, dance, name):
#         self.dance = dance
#         self.name = name


# obj = DancerEmployee("Bharatanatyam", "Priya")
# print(obj.name)
# print(obj.dance)
# obj.show()  # This will call the show method from Employee class due to method resolution order (MRO)
#             # i.e while inheriting we call the Employee class first


# Multilevel inheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name: {self.name} and Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")    
    
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "Golden Retriever")
        self.color = color
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
        
obj = GoldenRetriever("tommy", "Black")
obj.show_details()
