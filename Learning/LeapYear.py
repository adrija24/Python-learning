yr = int(input("Enter which year you want to check:\n"))
if yr % 100 == 0:
    if yr % 400 == 0:
        print("This is a leap year.")
    else:
        print("This is not a leap year")
elif yr % 4 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
