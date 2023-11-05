class Basic:
    def __init__(self, price):
        self.price = price
    
    def print_price(self):
        return self.price

class Fact:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, obj):
        return self.amount + obj.price

bs1 = Basic(100)
fc1 = Fact(50)
print(fc1+bs1)