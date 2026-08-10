class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))
    
p1 = Person.from_string("Ritesh-25")
print(p1.name, p1.age)
