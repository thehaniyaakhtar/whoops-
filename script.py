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
    def __init__(self, name, breed, owner):
    # init method, spl method, ran once when a class is instantiated
        self.name = name # attributes
        self.breed = breed
        self.owner = owner
        
    def bark(self): # method
        print("Whoof Whoof")
        
# different objects can be created with relation between them
class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number
        
owner1 = Owner("AA", "123 A", "432245")        
dog1 = Dog("A", "xyz", owner1) # creating a dog object of the dof class
                               # this is when __init__ runs

print(dog1.owner.name)
dog1.bark()
print(dog1.name)
print(dog1.breed)
# different dog objects can be created and acc

owner2 = Owner("BB", "345 AA", "123321")
dog2 = Dog("B", "hijk", owner2) # seperate object
dog2.bark()
print(dog2.name)
print(dog2.breed)

'''
recap:
a class is like a blueprint for an obj 
it defines what attributes/data/methods an object created from that class will have
An obj is an instance of a class
Attributes are variables that store info of the obj
methods are functions in  a class

self is used to access an objects methods and attributes inside the class
'''

class Person:
    # creating a person class
    # creating attributes inside it
    def __init__(self, name, age):
        self.name = name # attributes
        self.age = age
        
    # methods
    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old")
        
# objects
person1 = Person("Alice", 30)
person1.greet()

person2 = Person("Bob", 42)
person2.greet()

