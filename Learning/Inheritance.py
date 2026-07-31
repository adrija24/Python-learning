class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of employee {self.id} is {self.name}")
    
class Programmer(Employee):   #Inheritance, Programmer class is inheriting Employee class
    def showLanguage(self):
        print("the default language is Python")
e1 = Employee("Priya", 100)
e1.showDetails()

e2 = Programmer("Ronit", 101)
e2.showDetails()
e2.showLanguage()

