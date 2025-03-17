# name = input("Enter your name: ")
questions = [['\n1.How many continents are there on Earth?', 'a)Three', 'b)Seven', 'c)Four', 'd)Nine'],
             ['\n2.What is the largest planet in our solar system?', 'a)Jupitar', 'b)Venus', 'c)Mars', 'd)Earth'],
             ['\n3.Who wrote Romeo and Juliet?', 'a)Charles Dickens', 'b)Mary Shelley', 'c)William Shakespeare', 'd)Jane Austen'],
             ['\n4.What gas do plants absorb from the air?', 'a)Carbon Dioxide', 'b)Oxygen', 'c)Nitrogen', 'd)Methane'],
             ['\n5.How many legs does a spider have?', 'a)Four', 'b)six', 'c)Eight', 'd)Ten'],
             ['\n6.Which part of the human body pumps blood?', 'a)Heart', 'b)Lungs', 'c)Kidneys', 'd)Nerves'],
             ['\n7.What is the hardest natural substance on Earth?', 'a)Diamond', 'b)Gold', 'c)Granite', 'd)Silver'],
             ['\n8.What shape has four equal sides?', 'a)Circle', 'b)Rectangle', 'c)Square', 'd)Pentagon'],
             ['\n9.If you have 100 apples and give away 40, how many are left?', 'a)60', 'b)40', 'c)50', 'd)70'],
             ['\n10.What is the capital of France?', 'a)Lyon', 'b)Paris', 'c)Lille', 'd)Strasbourg']]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
answers = ['b', 'a', 'c', 'a', 'c', 'a', 'a', 'c', 'a', 'b']
money = 0
for i in range(0, len(questions)):
    print(f"\nQuestion for Rs. {levels[i]} is: ")
    print(questions[i][0])
    print(f"Options are:\n{questions[i][1]}\n{questions[i][2]}\n{questions[i][3]}\n{questions[i][4]}")
    ans = input("\nEnter your answer(Write a or b or c or d): ")
    if ans == answers[i]:
        money = money + levels[i]
    else:
        print("Wrong answer")
print(f"You get Rs. {money}")