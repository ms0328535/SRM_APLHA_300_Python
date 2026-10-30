def hello():
    print("hello")
def Hello(name):
    print(f"Hello my name is {name}")
Hello("Murali")

def HELLO(name="My friend"):
    print(f"Hello {name}")
HELLO()

def change(val):
    val = 2
val = 1
change(val)

print(val)

# Dictionary Format

def change(value):
    value['name']='syd'
val = {"name":"Beau"}
change(val)

print(val)

# Variable Scope in Function
age = 12
def test():
    print(age)
test()
print(age)

# nested function example

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)
talk("I am going to buy milk!")

def counter():
    count=0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment
increment = counter()

