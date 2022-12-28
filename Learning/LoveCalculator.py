print("Welcome to the love calculator!")
name1 = (input("What is your name?\n")).lower()
name2 = (input("What is his/her name?\n")).lower()
new_name = name1 + name2

#count for name1
t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")

l = new_name.count("l")
o = new_name.count("o")
v = new_name.count("v")
E = new_name.count ("e")

true = t+r+u+e
love = l + o + v + E
score = ((true*10) + love)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")