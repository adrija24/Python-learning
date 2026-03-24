a = input("Enter a value between 5 to 8 or write quit: ")

if (a != "quit" and (int(a) < 5 or int(a) > 8)):
    raise ValueError("Value must be between 5 and 8.")

print("Value is valid.")