import random
user_score = 0
computer_score = 0
round = int(input("Enter how many rounds you want to play this game:\n"))
for i in range(round):
    user_ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
    print("Your choice is: ", end="")
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
        user_score += 1
    else:
        computer_score += 1
    print(f"Your score is {user_score}")
    print(f"Computer's score is {computer_score}")

if user_score == computer_score:
    print("You had a draw!!!")
elif user_score > computer_score:
    print("You win!!!")
else:
    print("You lost the game.")