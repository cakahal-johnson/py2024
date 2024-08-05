"""
A Lambda Function is a small anonymous function which can take any number of arguments, but can only have one expression
Syntax:
Lambda arguments : expression
where the expression is executed and the result is returned...
"""

# x = lambda a: a + 10
# print(x(5))  # 15
#
# # Multiply argument where b with argument c and return the result
# e = lambda b, c: b * c
# print(e(5, 6))  # 30
#
# f = lambda g, h, j: g+h+j
# print(f(5, 6, 2))

"""
Why USING LAMBDA FUNCTION
With the power of Lambda is better show when you use them as an anonymous function inside another function

where we have a function definition that takes one arguments, and that arguments will multiplied with an unknown numbers 

"""

def myFunc(n):
    return lambda k: k * n

myVar = myFunc(2)
myVar1 = myFunc(3)

print(myVar(11))  #22
print(myVar1(11)) #33

# we use lambda function when an anonymous function is required for a short period of time...

"""
PYTHON CLASSES/OBJECTS(OOP)
Python is an Object oriented programming language
where A class is like an Object constructor, or a "blueprint" for creating objects

Almost everything python is an object, with its properties and methods

"""

# creating a Class: we use the keyword class
class myClass:
    x = 5

p1 = myClass()
print(p1.x) # 5

#  __init__() Function
"""
with the above classes and object in their simplest form, are not really useful in real life applications

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes hava a function __init__(), which is always executed when the class is being initiated

we use the __init__() function to assign values to object properties, or other operations that are necessary to do when
when the object is create 

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myPlayer(abc):
        print(("Hello is nice to meet you! " + abc.name))


player1 = Person("Johnson", 90)
player1.age = 40

print(player1.name)
print(player1.age)

player1.myPlayer()


# pass
class Person2:
    pass

"""
Using the super() function'
will make the child inherit all the methods and properties from it's parent

"""

class Person3:
    def __init__(self, fanme, lname):
        self.firstname = fanme
        self.lastname = lname

    def myFullname(self):
        print(self.firstname, self.lastname)

    # here we add the child class
class Student(Person3):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def Welcome(self):
        print("Welcome ", self.firstname, self.lastname, "to the class of ", self.graduationYear)


a = Person3("Cakahal", " Johnson")
a.myFullname()

b = Student("Regal", "Victor", 2020)
b.myFullname()
# b.Welcome()

c = Student("Peter", "Obi", 2211)
c.myFullname()
print(c.graduationYear)
c.Welcome()

print(b.graduationYear)





