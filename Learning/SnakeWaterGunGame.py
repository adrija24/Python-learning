# My solution
import random

user_result = 0
com_result = 0
count = 1
while(count <= 5):
    user_input = int(input("Enter 1 for Snake, 2 for Water and 3 for Gun: "))
    com_input = random.randint(1, 3)
    print(f"Computer chose: {com_input}")
    if user_input == com_input:
        print("It's a tie!")
    elif user_input == 1 and com_input == 2:
        print("You win! Water destroys gun.")
        user_result += 1
    elif user_input == 3 and com_input == 1:
        print("You win! Gun kills snake.")
        user_result += 1
    else:
        print("Computer wins!")
        com_result += 1
    count += 1

print(f"Final Score - You: {user_result}, Computer: {com_result}")
if user_result > com_result:
    print("Congratulations! You won the game.")
elif com_result > user_result:
    print("Sorry, you lost the game.")
else:
    print("The game is a tie.")
    
    

# Harry's solution
def check(com, user):
    if(com == user):
        return 0
    elif((com == 1 and user == 2) or (com == 2 and user == 3) or (com == 3 and user == 1)):
        return -1
    else:
        return 1
com_input = random.randint(1, 3)
user_input = int(input("Enter 1 for Snake, 2 for Water and 3 for Gun: "))

score = check(com_input, user_input)
print(f"Computer: {com_input}")
print(f"You: {user_input}")
if(score == 0):
    print("It's a tie!")
elif(score == 1):
    print("You win!")
else:
    print("Computer wins!")