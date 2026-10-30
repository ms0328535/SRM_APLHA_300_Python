name="murali";print(name)
# or
school = "Srm"
print(school)
print(isinstance(name,int))
# built in datatypes (type or isinstance)
# class string 
# class integer
# class float
# important note : {we can convert the string to integer Ex:{int("20")}}
# arithmetic operators including {+,-,*,/,%,**,//}
print(1+-1)
# comparison operators including {==,!=,>,<,<=,>=} returns boolean values
print(2==2)
# Bitwise Operators including {&,|,^,~,<<,>>}
# ternary operators including 
def is_adult(age):
    return True if age>18 else False

# Strings in Python:
print("""    Beau
is 18 years old
""")
print("be\"au")
# String methods
print("beau".upper())
print("Beau".lower())
print("beau person".title())

# isalpha() , isalnum(), isdecimal(), startswith(), endswith(), join(), find()

# String character and slicing
print(name[1:2]);print(name[-1:-2])

# Boolean Example

done = 0
if done:
    print("yes")
else:
    print("no")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])

print(read_any_book)

book_1_read = True
book_2_read = False

read_any_book = all([book_1_read, book_2_read])

print(read_any_book)

# number datatypes
num1 = 2+3j
num2 = complex(2,3)
print(num2.real,num2.imag)


# built in function

print(abs(5.5));print(round(3.6));print(round(5.49,1))

# enums

from enum import Enum 

class State(Enum):
    Inactive = 0
    Active = 1

print(State(1))
print(len(State));print(list(State))

# Lists {set of elements}

dogs = ["roger",1,"syd",True];print(dogs[2])

# methods including in the lists : {append("object added at the last")
#                                   extend("add all the elements of another iterable")
#                                   +=("Each letter in a word is printed")
#                                   remove("removing the element")
#                                   pop("roving the element by index value")
#                                   insert("Inserting the elements")
#                                   sort("arranging the elements by ascending")}

# Tuples {Not modified after need to change}

names = ("roger",20)
names.index('roger')
len(names)

# Dictionary {contains keys and values,also various datatypes is stored in single dictionary is applicable}

dog = {"name":"nubs","age":8}
print(dog['name']);print(dog.popitem());print(dog.keys());print(dog.values())

# set operation performance

set1 = {"Roger","Syd"}
set2 = {"Roger"}

intersect = set1 & set2
mod = set1-set2;mod = set1>set2
print(intersect)


# Loops in python

# while condition

count = 0
while count < 10:
    print("The condition is True")
    count += 1
print("After the Loop")

# for loop
item = [1,2,3,5]
for index,item in enumerate(item):
    print(index,item)