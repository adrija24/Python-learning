print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age:\n"))
    if age < 12:
        print("Please pay 5Rs.")
    elif age <= 18:
        print("Please pay 10Rs.")
    else:
        print("Please pay 20Rs.")
else:
    print("Sorry! You can't ride the tollercoaster.")
