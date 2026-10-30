multiply = lambda a,b : a*b

print(multiply(2,4))

# Map and Filters in Python
double = lambda a : a*2
numbers = [1,2,3]
result = map(double,numbers)

print(list(result))

def iseven(n):
    return n%2 == 0
result = filter(iseven,numbers)

print(list(result))

from functools import reduce

expenses = [
    ('Dinner',80),
    ('Car Repair',120)
]
sum = reduce(lambda a,b : a[1]+b[1],expenses)
print(sum)