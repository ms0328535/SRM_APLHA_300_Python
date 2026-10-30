# Positional, keyword, default
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sam"))
print(greet(greeting="Hi", name="Sam"))

# Positional-only (/) and keyword-only (*)
def f(a, b, /, c, *, d):
    print(a, b, c, d)

f(1, 2, 3, d=4)
f(1, 2, c=3, d=4)
# f(a=1, b=2, c=3, d=4)   # error: a and b are positional-only

# *args and **kwargs
def show(*args, **kwargs):
    print(args)        # tuple
    print(kwargs)      # dict

show(1, 2, 3, x=10, y=20)

# Unpacking into a call
def add3(a, b, c): return a + b + c
print(add3(*[1, 2, 3]))
print(add3(**{"a": 1, "b": 2, "c": 3}))

# Mutable default argument trap
def bad(item, bucket=[]):
    bucket.append(item); return bucket
print(bad(1), bad(2))        # [1, 2] [1, 2] (shared list!)

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item); return bucket

# Pass-by-object-reference behavior
def modify(lst, num):
    lst.append(99)       # mutates the original list
    num += 1             # only rebinds the local name

my_list, my_num = [1], 5
modify(my_list, my_num)
print(my_list, my_num)   # [1, 99] 5

# Variable scope
x = 10
def change():
    global x
    x = 20