num = len(input("What is your name?\n"))

#print("The length of your name is " + num + " characters")    #It will give an error because we can't concatenate an string with an integer

#To know the type of the input we can use
print(type(num))

#Typecasting
#Process 1
new_num = str(num)
print("The length of your name is " + new_num + " characters")

#Process 2
char = str(len(input("Write your name\n")))
print("Your name has " + char + " characters")

#Process 3
print("The no of characters in your name is " + str(len(input("What is your name?\n"))))