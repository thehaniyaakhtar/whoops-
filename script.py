# Everything created in python is an object
name = "Danny"
age = 89

# objects are made from classes
# classes define what an object should look like

print(type(name)) 
print(type(age))   # int obj, made from class int

# diff objects have different behaviors, functions/ methods
# allows to maniplate data

a = name.upper()
print(a)
b = age.bit_length()
print(a)
print(b)

# we can also create our own class and instances from those classes
class Doggy:
    def bark(self):
        print("Woof Woof")
        # definng methods and atributes of a class
doggy = Doggy()
# variable with an insstance assigned to it
# by calling the class name

# accessing methos on obj:
doggy.bark()


class Dog: # dog class 
    def __init__(self, name, breed):
    # init method, spl method, ran once when an obj is instantiated
        self.name = name
        self.breed = breed
        
    def bark(self):
        print("Whoof Whoof")
        
dog1 = Dog("A", "xyz") # creating a dog object
                       # this is when __init__ runs
dog1.bark()
print(dog1.name)
print(dog1.breed)
# different dog objects can be created and acc

dog2 = Dog("B", "hijk")
dog2.bark()
print(dog1.name)
print(dog1.breed)