import random
user_ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if user_ch == 0:
    print("Rock")
elif user_ch == 1:
    print("Paper")
elif user_ch == 2:
    print("Scissor")
comp_ch = random.randint(0, 2)
if comp_ch == 0:
    print("Rock")
elif comp_ch == 1:
    print("Paper") 
elif comp_ch == 2:
    print("Scissor")   

if user_ch == comp_ch:
    print("You had a draw!!!")
elif user_ch == 0 and comp_ch == 2 or user_ch == 1 and comp_ch == 0 or user_ch == 2 and comp_ch == 1:
    print("You win!!!")
else:
    print("You lost the game.")