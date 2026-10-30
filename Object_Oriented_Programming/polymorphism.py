class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

class Robot(Dog):
    def speak(self): return "Beep " + super().speak()

for animal in [Dog(), Cat(), Robot()]:
    print(animal.speak())            # same call, different results

# Built-ins are polymorphic too
print(len("hello"), len([1, 2, 3]), len({"a": 1}))