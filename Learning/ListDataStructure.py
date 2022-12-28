#We can create a list without creating different variable
fruits = ["Mango", "Apple", "Banana"]
print(fruits)

#to print the first item in the list
print(fruits[0])

#to print the last item in the list
print(fruits[-1])  

#to add a single item after the last item
fruits.append("Guava")
print(fruits)

#to add multiple items after the last item
fruits.extend(["Orange", "Watermelon"])
print(fruits)