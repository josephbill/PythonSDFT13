'''
Getter and setter methods in python are used to access and modify 
private instance variables.
- Traditional get_attribute and set_attribute name 
- Pythonic way is to use the @property decorator for getter methods
- @atrributename.setter decorator for setter methods
'''
class Dog:
    def __init__(self,name):
        self.__name = name
        
    #getter method 
    def get_name(self):
        return self.__name
    #setter 
    def set_name(self, name):
        if len(name) > 0:
            self.__name = name 
            return self.__name
        else:
            print("Name cannot be empty")
            
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if len(name) > 0:
            self.__name = name
            return self.__name
        else:
            print("Name cannot be empty")
    
    @name.deleter
    def name(self):
        del self.__name
        print("Name deleted")
    
dog1 = Dog("Buddy")
print(dog1.get_name())
print(dog1.set_name("Max"))
print(dog1.get_name())
print(dog1.name)
dog1.name = "Charlie"
print(dog1.name)
del dog1.name
print(dog1.name)
