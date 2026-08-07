class Student:
    college = "ABC College"      #Class variable

    def __init__(self, name):
        self.name = name        #Instance variable
    
    def showDetails(self):
        print(f"The name of the student is {self.name} and the college is {self.college}")

s1 = Student("Adrija")
s1.name = "Priya"
s1.showDetails()
s2 = Student("Rahul")
s2.showDetails()

Student.college = "XYZ College"
s1.showDetails()
s2.showDetails()

s1.college = "PQR College"
s1.showDetails()
s2.showDetails()
