# A class is a blueprint, an object is one thing built from it
class Item:
    def calculate_total_price(self, price, quantity):
        return price * quantity

item1 = Item()
item1.name = "Phone"            # attributes assigned after creation
item1.price = 100
item1.quantity = 5

print(item1.calculate_total_price(item1.price, item1.quantity))   # 500
print(type(item1))              # <class '__main__.Item'>


# Constructors

class Item:
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Validate the received arguments
        assert price >= 0, f"Price {price} must be zero or greater"
        assert quantity >= 0, f"Quantity {quantity} must be zero or greater"

        # Assign to the object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
print(item1.calculate_total_price())    # 500
print(item2.calculate_total_price())    # 3000

# Item("Cable", -5)   # AssertionError with our message

# Attributes

class Item:
    pay_rate = 0.8          # class attribute: shared by all objects
    all = []                # track every instance

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def apply_discount(self):
        self.price = self.price * self.pay_rate    # uses class or instance value

    def __repr__(self):
        return f"Item({self.name!r}, {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(Item.pay_rate)                  # 0.8
print(item1.__dict__)                 # instance attributes only
print(Item.__dict__.keys())           # class-level attributes

item2.pay_rate = 0.7                  # instance override, doesn't affect others
item2.apply_discount()
print(item2.price, item1.pay_rate)    # 700.0 0.8
print(Item.all)                       # uses __repr__

# Class vs Static Methods

import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    # Class method: first argument is the class itself
    @classmethod
    def instantiate_from_csv(cls, path="items.csv"):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                cls(
                    name=row.get("name"),
                    price=float(row.get("price")),
                    quantity=int(row.get("quantity")),
                )

    # Static method: no self or cls, just a utility tied to the class
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.price}, {self.quantity})"

print(Item.is_integer(7.0))    # True
print(Item.is_integer(7.5))    # False
print(Item.is_integer(7))      # True

# items.csv example:
# name,price,quantity
# Phone,100,1
# Laptop,1000,3
# Item.instantiate_from_csv()
# print(Item.all)