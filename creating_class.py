# Define a class Item
class Item:
    
    # Method to calculate total price
    # self refers to current object
    def calculate_total_price(self, x, y):
        return x * y

# Create first object of Item
item1 = Item()

# Assign atributes to item1
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# Call method using item and print total price
print(item1.calculate_total_price(item1.price, item1.quantity))

# Create second object of Item
item2 = Item()

# Assign attribute to item2
item2.name = "Laptop"
item2.price = 500
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

# Defining a class conventionally
class Item:
    pay_rate = 0.8
    def __init__(self, name, price: float, quantity=0):
        # data type can also be declared
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0  # no custom error message
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
# When no default value was passed
# item1 = Item("Phone", 100, 2)
# item2 = Item("Laptop", 100, 1)

# When default value is passed
item1 = Item("Phone", 100)

# can be overridden
item2 = Item("Laptop", 100, 3)
item2.apply_discount()
# to give custom discount rate
# item2.pay_rate = 0.7
print(item2.price)

print(item1.name)
print(item2.name)

print(item1.price)
print(item2.price)

print(item1.calculate_total_price()) # 0
print(item2.calculate_total_price())


