### OOP : Object Oriented Programming 

RDBMS

Database 
     - Tables  -> rows (records) and columns(fields or props of the records)

     - users : id, name, admission number , role 
                1, Joseph, 48394, TM 
                2, Kibet, 84398, student 

                functions to interact with the database 
                = function create 
                = function display 
                = function updates 
                = function delete
     - courses : id, name , course id , description
                = function create 
                = function display .... 
                = function update 
EVERYTHING IN PYTHON IS AN OBJECT 

x = "Joseph"
y = "10"

x.lower()
y.lower()

OOP is a programming paradigm that organizes code into objects that 
contain both data (attributes) and behaviours (methods/functions). 

- make ,model, color ,yom  - blueprints character... of a car : attributes
  Toyota , Corolla, white , 2006 
  Toyota, X , black , 2004 

- accelarate :  , break , engine_capacity , : behaviours 

### FOUR PILLARS OF OOP 
1. Encapsulation: bundle data and methods that operate on that data into one unit 

class Vehicle:
     bundle associated data and methods 

2. Abstraction : Hides complex implementation details and shows only 
essential features 
3. Inheritance : Creating new blueprints (class) from existing ones 
4. Polymorphism : using a single interface for diff. data types 


### ACCESS MODIFIERS 
control the visibility and accessibility of class members (attributes and methods)
Python doesn't enforce strict access like some other languages e.g java and c++ , it uses naming conventions to suggest intended access.

1. Public members  = everything is public unless explicilty made private or protected 

2. Protected members  = intended for internal use or subclasses(inheritance)
_NameAttribute
_Nameoffunction

3. Private members = python internally changes the name of the attribute to _CLASSNAME__ATTRIBUTE , access is blocked from outside on 
use of the original attribute name 
__NameAttribute 
__NameofFunction