print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
p = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n") )
amount = ((((p / 100) * bill) / people))
#new_amount = "{:.2f}".format(amount)
print(f"Each person should pay {round(amount,2)}")