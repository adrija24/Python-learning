names = ['Alice', 'Bob', 'Charlie', 'David']
for index, name in enumerate(names):
    print(f"Index: {index}, Value: {name}")

marks = [85, 92, 78, 90]
for index, mark in enumerate(marks):
    print(mark, "Awesome!") if index == 1 else print(mark)