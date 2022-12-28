import random
names = input("Give me everybody's names, seperated by a comma.\n")
names = names.split(", ")
len = (len(names))

# print(f"{names[random.randint(0, len - 1)]} will pay the bill")
print(f"{random.choice(names)} will pay the bill")    #We can write only this line