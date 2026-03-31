#MAP
l = [1, 2, 3, 4, 3, 5]
def cube(x):
    return x * x * x
print(cube(2))

newl = list(map(lambda x: x * x, l))
print(newl)
newl = list(map(cube, l))
print(newl)

#FILTER
def func(a):
    return a > 3

list2 = list(filter(func, l))
list3 = list(filter(lambda x: x > 2, l))
print(list2)
print(list3)

#REDUCE
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)