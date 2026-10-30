class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.price}, {self.quantity})"


class Phone(Item):                         # child class
    def __init__(self, name, price, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)   # reuse the parent's constructor
        assert broken_phones >= 0, "Broken phones can't be negative"
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())      # inherited method: 2500
print(Phone.all)                           # inherited class attribute
print(isinstance(phone1, Item))            # True
print(Phone.__mro__)                       # method resolution order