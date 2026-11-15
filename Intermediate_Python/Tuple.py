import sys
import timeit

#tuple are immutable , allow dupicates , ordered
tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional


tuple_3 = (25,)#if only one element there should be a coma or it is considered as int
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4)

#access elements

print(tuple_1[0])
print(tuple_1[-1])

#Adding or changing the tuple

#tuple_1[2] = "Boston" #gives TypeError

#delete tuple

del tuple_2

#iterating

for i in tuple_1:
    print(i)

#check if an element exist

if "New York" in tuple_1:
    print("yes")
else:
    print("no")

my_tuple = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple = ('a', 'b') * 5
print(my_tuple)

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)

#slicing

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3]
print(b)
b = a[2:] 
print(b)
b = a[:3] 
print(b)
b = a[::2] 
print(b)
b = a[::-1]
print(b)

#unpacking tuple
    #for fixed size element
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)

    #for Variable size element
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)

#nested loop

a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])

#list and tuple camparision

#gives the sizes
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

#Gives the time of excution
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))