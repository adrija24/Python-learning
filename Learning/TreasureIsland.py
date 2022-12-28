print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
road = (input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")).lower()
if road == "right":
    print("Game over.")
else:
    lake = (input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")).lower()
    if lake == "swim":
        print("Game over.")
    else:
        door = (input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?\n")).lower()
        if door == "red":
            print("Game over.")
        elif door == "blue":
            print("Game over.")
        else:
            print("You win!!!")