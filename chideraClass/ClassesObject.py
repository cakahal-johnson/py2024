"""
Python Classes/Objects

Python is an Object oriented programming language

Almost everything in Python is an Object, with its properties and methods

A class is like an object constructor, or a "blueprint" for creating objects.

To create a class, we use the keyword class:
example: below will hit an error be'cos is not an Object
class MyClass:
    x = 5
print(MyClass)

output: <class '__main__.MyClass'>

"""


class MyClass:
    x = 5


v1 = MyClass()

# MyClass = 5
# print(v1.x)


"""

 __init__() Function
since the above function is not really useful in real life applications then to understand the meaning of Classes we have
to understand the built-in __init__() Function

by knowing That All classes have a function called __init__(), which is always executed when the class is being initiated.

so, we use __init__() function to assign values to objects properties, or other operations that are necessary to do
when the object is being created:

Example: Where we Create a class named Person, use the __init__() function to assign values for name and age: 

classes is the noun:

"""
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myFunc(self):
#         print("Hello my name is: " + self.name)
#
#
# p1 = Person("Cakahal Johnson", 70)
# p1.myFunc()
# p2 = Person("Chidera", 700)
# p3 = Person("Computer Player", 70000)
#
#
# print(p1.name, p1.age)
# # print(p1.age)
#
# print(p3.age, p3.name)
#
# print(p1.name, p2.name)


"""
Object Methods this is the verb:
Objects can also contain methods. Methods in objects are functions that belong to the object

lets us create a method in the Person Class:

Example: where we insert a function that prints a greeting, and execute it on the p1 object above

NB: self: in a parameter is a reference to the current instance of the class, and is used to access variables
that belong to the class

The self Parameter:
The self parameter is a reference to the current instance of the class, and is used to access variables that belong
to the class.

it does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any
function in the class

Example: Use words mysillyobject and abc instead of self parameter: 
 

"""


# class Person:
#     def __init__(abc, name, age):
#         abc.name = name
#         abc.age = age
#
#     def myFunc(abc1):
#         print("Hello my name is: " + abc1.name)
#
#
# p1 = Person("Cakahal Johnson", 70)
# p1.myFunc()


#  Modify Object Properties
# you can modify properties on objects like this:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myFunc(self):
#         print("Hello my name is: " + self.name)
#
#
# p1 = Person("Cakahal Johnson", 70)
# p1.age =100
#
# print(p1.age)


# DELETING OBJECT PROPERTIES
# You can delete properties on objects by using the del Keyword
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is: " + self.name)


p1 = Person("Cakahal Johnson", 70)
del p1.age

print(p1.age) #This will give an error message: saying AttributeErroe: 'person' object has no attribute 'age'

# THE PASS STATEMENT
# clss definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass
# statement to avoid getting an error.


class PerSon:
    pass
    # having an empty class definition like this, would raise an error without the pass statement


