"""
A lambda function is a small anonymous function which can take any number of agruments, but can only have one expression
Syntax:
lambda arguments : expression

where the expression is executed and the result is returned...


"""

x = lambda a : a + 10
print(x(5)) # 15

# Multiply argument where b with argument c and returns the result
e = lambda b, c : b * c
print(e(5, 6)) # 30

# sumamarizing an Argument
f = lambda g, h, j : g + h + j
print(f(5, 6, 2))

"""
WHY USING LAMBDA FUNCTION
the power of lambda is better show when you use them as an anonymous function inside function

where we have a function definition that takes one arguments, and that arguments will be multiplied with an unkown number


"""


def myFunc(n):
    return lambda k: k * n


myNum = myFunc(2)
myNum2 = myFunc(3)

# now lets add whatever we want to output
print(myNum(11))  # returns 2 x 11 = 22
print(myNum2(11))  # returns 3 x 11 = 33

# NB: we lambda function when an anonymous function is required for a short period of time...

"""
Next Class CLASSES / OBJECTS (OOP) OBJECT ORIENTED PROGRAMMING
python is an object oriented programming language
where A class is like an Object constructor, or a "blueprint" for creating objects

Almost everything in python is an Object, with its properties and methods

"""


# Creating a Class: we use the keyword 'Class'
class myDemo:
    x = 5


player = myDemo()
print(player.x) # 5


# __init__() function
"""
with the above classes and object in their simplest form, and are not really useful in real life application

To understand the meaning classes we have to understand the built-in __init__() function

All classes have a function called __init__(), which is always executed when the class is being initiated

we use the __init__() function to assign values to object properties, or other operations that are necessary to do when 
the object is created

"""


class Person1:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age


player11 = Person1("Johnson", 70)  # here we call out the function
print(player11.Name)
print(player11.Age)


"""
Objects can also contain methods in objects and function that belong to the object
lets insert a function that prints a greeting, and execute it on the player1
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myGreet(self):
        print("Hello is nice to meet! " + self.name)


player1 = Person("Cakahal", 70)

player1.myGreet()  #  this will call function b'cos the function is having a print already


"""
the self parameter is a reference to the current instance of the class, and is used to access variables that belongs class

it does not have to be named self, you can call it whatever you like, but is has to be the first parameter of any 
function in the class

"""