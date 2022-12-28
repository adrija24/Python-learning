print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age:\n"))
    if age < 12:
        bill = 5
        print(f"Please pay {bill}Rs.")
    elif age <= 18:
        bill = 10
        print(f"Please pay {bill}Rs.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us.")
    else:
        bill = 20
        print(f"Please pay {bill}Rs.")
    photo = input("Do you want a photo taken? Y or N.\n")
    if photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}Rs")
else:
    print("Sorry! You can't ride the rollercoaster.")
