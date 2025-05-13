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
    # Public members are accessible from outside the class
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
    def __init__(self,name,age,mood):
        super().__init__(name,age)
        self.__mood = mood
    # dog has access to the attributes and methods of the animal class 
    def _adjust_mood(self, mood):
        # private members are not accessible from outside the class
        self.__mood = mood
        return f"{self.name} is now {self.__mood}."
    
    # adjust_mood as a helper method inside my class or on inherited 
    #sub class 

class Cat(Animal):
    def __init__(self,name, age, breed):
        super().__init__(name, age) #calling the constructor of the parent class
        self.breed = breed
        self.__diet = "meat"
    # private members are not accessible from outside the class
    def __adjust_diet(self, diet):
        self.__diet = diet
        return f"{self.name} is now on a {self.__diet} diet."
    
 
cat1 = Cat("Garfield",2,"Persian") 
cat1.__diet = "vegetarian"
print(cat1._Cat__diet)  # name mangling _classname__PrivateVariable 

# creating an instance of the Dog class
dog1 = Dog("Buddy", 3,"happy")
print(dog1.__mood)

# dog2 = Dog("Max", 5)
# accessing the instance attributes 
# print(dog1.name)
# print(dog1.age)
# print(dog1.sound("woof"))
# print(dog1.species)
# dog1.__mood = "angry"

# cat1 = Cat("Whiskers", 2)
# print(cat1.name)
# print(cat1.sound("meow"))
    
class String:
    def __init__(self,value):
        self.value = value 
        
    def lower(self):
        #process the logic to transform a string to lower case
        pass
    
    
x = String("HELLO")
x = "sjkdksjd"