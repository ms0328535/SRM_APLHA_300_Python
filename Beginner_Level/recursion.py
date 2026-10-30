def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

#Decorator
def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("Hello")


