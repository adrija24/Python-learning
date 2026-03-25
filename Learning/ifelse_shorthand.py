a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"{a} is greater than {b}") if a > b else print(f"{b} is greater than {a}") if b > a else print(f"{a} and {b} are equal")