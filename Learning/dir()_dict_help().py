# #dir()
# x = [1, 2, 3]
# print(dir(x))

#__dict__
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = person("Dinesh", 30)
# print(p.__dict__)

#help()
print(help(person))