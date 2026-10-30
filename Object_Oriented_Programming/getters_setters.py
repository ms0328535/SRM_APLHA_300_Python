class Item:
    def __init__(self, name, price, quantity=0):
        self.__name = name                 # double underscore: name-mangled "private"
        self.price = price
        self.quantity = quantity

    # Read-only attribute
    @property
    def name(self):
        return self.__name

    # Setter with validation
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise ValueError("Name is too long (max 10 characters)")
        self.__name = value

    # Computed property
    @property
    def total(self):
        return self.price * self.quantity

item = Item("Phone", 100, 2)
print(item.name)           # uses the getter
item.name = "Laptop"       # uses the setter
print(item.total)          # 200, no parentheses needed
# item.name = "ThisNameIsTooLong"   # ValueError