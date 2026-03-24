a = input("Enter a number: ")

try:
    print(f"Multiplication Table of {a} is:")
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a) * i}")
except ValueError as e:
    print(e)

print("Program ended.")

