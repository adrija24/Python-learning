class person:  #creating a class
    name = "John"
    age = 36
    occupation = "programmer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")  #The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class.

p1 = person() #creating an object of class person
p1.name = "Rana" #The informations that we will not give in the object those will be taken from the main class.

print(p1.name)
print(p1.age)
print(p1.occupation)
p1.info()

