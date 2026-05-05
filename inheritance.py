# class Item has all attributes that we need + broken_phones which 
# will be creaeted in the new class

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name, price, quantity):
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self) 
        
    def calculate_total_price(self):
        return self.price * self.quantity
    # parent class

    def apply_discount(self):
        self.price = self.price * self.pay_rate        


class Phone(Item): # Phone is a type of Item
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        super().__init__(
            name, price, quantity
        )
        # calls the parent class constructor and runs all the attributes internally
        
        assert broken_phones >= 0
        
        self.broken_phones = broken_phones
        
    def apply_discount(self):
        self.price = self.price * 0.5
        # child class
        # the parent class is overridden

phone1 = Item("ABC", 500, 5, 1)

print(Item.all)