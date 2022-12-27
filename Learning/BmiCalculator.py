h = input("Enter your height in meter:\n")
w = input("Enter your weight in kg:\n")
nw = float(w)
nh = float(h)
BMI = nw / (nh ** 2)
if BMI < 18.5:
    print(f"Your BMI is {round(BMI, 2)}, You have an underweight")
elif BMI < 25:
    print(f"Your BMI is {round(BMI, 2)}, you have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {round(BMI, 2)}, you have an overweight")
elif BMI < 35:
    print(f"Your BMI is {round(BMI, 2)}, you have an obese")
else:
    print(f"Your BMI is {round(BMI, 2)}, you are clinically obese")   