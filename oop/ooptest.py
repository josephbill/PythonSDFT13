# A class is a blueprint for creating objects
# An object is an instance of a class
# an attiribute is a variable that belongs to a class
# attributes are of two types : class attributes: attribute belongs 
# to the blueprint/class and instance attributes:
# data that belongs to all instance created from the class 
class Animal:
    #class attributes 
    species = ""
    # instance attributes 
    # normally defined in the constructor 
    # self is a keyword that refers to the current instance being processed 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    # methods are functions that belong to a class
    # instance methods are identified with the first parameter as self
    def sound(self, sound):
        return f"{self.name} says {sound}!"
    
    def describe(self):
        return f"{self.name} is {self.age} years old."
    
class Dog(Animal):
    # dog has access to the attributes and methods of the animal class 
    pass

class Cat(Animal):
    pass
    
    
# creating an instance of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
# accessing the instance attributes 
print(dog1.name)
print(dog1.age)
print(dog1.sound("woof"))
print(dog1.species)

cat1 = Cat("Whiskers", 2)
print(cat1.name)
print(cat1.sound("meow"))
    
class String:
    def __init__(self,value):
        self.value = value 
        
    def lower(self):
        #process the logic to transform a string to lower case
        pass
    
    
x = String("HELLO")
x = "sjkdksjd"