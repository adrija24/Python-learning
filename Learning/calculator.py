num_1 = int(input("Enter the first number:\n"))
num_2 = int(input("Enter the second number:\n"))
result = int(input("Enter 1 for add, 2 for subtract, 3 for multiply, 4 for exponential, 5 for modulus or 6 for floor division:\n"))
if result == 1:
    print(num_1 + num_2)
elif result == 2:
    print(num_1 - num_2)
elif result == 3:
    print(num_1 * num_2)
elif result == 4:
    print(num_1 / num_2)
elif result == 5:
    print(num_1 % num_2)
elif result == 6:
    print(num_1 // num_2)