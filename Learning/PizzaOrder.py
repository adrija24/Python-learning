print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
pepperoni = input("Do you want pepperoni? Y or N\n")
cheese = input("Do you want extra cheese? Y or No\n")
price = 0
if size == "S":
    price += 50
    if pepperoni == "Y":
        price += 10
elif size == "M":
    price += 60
    if pepperoni == "Y":
        price += 20
elif size == "L":
    price += 100
    if pepperoni == "Y":
        price += 20
#We can also do this to calculate pepperoni price
#if pepperoni == "Y":
#    if size == "S":
#        price += 10
#    else:
#        price +=20

if cheese == "Y":
    price += 10
print(f"Your final bill is {price}Rs.")