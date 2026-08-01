# Public Access Modifier
class Employee:
    def __init__(self):
        self.name = "Adri"   #Public variable
a = Employee()
print(a.name)  

# Private Access Modifier
class Employee:
    def __init__(self):
        self.__name = "Adri"   #Private variable

a = Employee()
# print(a.__name)  # Cannot be accessed directly
print(a._Employee__name)  # Can be accessed indirectly using name mangling

# Protected Access Modifier
class Student:
    def __init__(self):
        self._name = "Adri"   # Protected variable
    
    def _funName(self):       # Protected method
        return "CodeWithAdri"

class Subject(Student):       # inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())

# calling by object of Subject class
print(obj1._name)
print(obj1._funName())