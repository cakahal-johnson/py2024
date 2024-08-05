import random

print("cakahal johnson says welcome to python")

print()

if 10 > 2:
    print("yes 10 is greater than 2")
if 2 > 10:
    print("No 10 is greater")

# python comments
# python comments single line comment

"""
isksisisisiiss
sskjksjsjsjs
jsksskisks
this is for multiline comments

"""

# shortcut for is ctrl / placed in the line code

#   PYTHON VARIABLES
"""
variable is like a containers for storing data values

Rules of assigning a variable
1. camel-case,  pascal-case, snake-case,     upper-case,    word-n-number
    myVar,       my_var        MyVar,           MYVAR           myvar1
    
illegal ways: number-before-word, using a - , using a white-space...
                2myvar              my-var,     my var
                
"""

name = "cakahal"
age = 70
print(name)
print(age)

# concatination this combine two var both text and number
# we use: + character;

Name = "Johnson"
print("My name is: " + name + " " + Name)

# casting into a d/f datatype
word = str(3)
number = int(3)
dic = float(3)

print(dic)
print(number)
print(word)

# GETTING THE CASTED DATATYPE
print(type(word))
print(type(dic))
print(type(number))

# Multiple Variable
print("My name is cakahal johnson i love python")

x, y, z = "benz", "lexus", "bus"
print(x)
print(y)
print(z)

car = ["benz", "lexus", "venza"]

a, b, c = car
print(a)
print(b)
print(c)

add = 450
add1 = 252
# add2 = "Answer is: "
summ = add * add1
print(summ)

# Global Keyword
# when you create a variable inside a function, that the is local, and can only be used inside that function
# To create a global variable inside a function, you can use the global keyword


def myName():
    global d
    d = "cakahal"

myName()
print(d)
print("my name is " + d)
print("my best friend is 6868 " + d)
print("i'm Johnson and my first name is: " + d)


nameVar = "cakahal Johnson"
print(nameVar)


def Myfunc():
    global nameVar
    nameVar = "sir P"

Myfunc()
print("my name is " + nameVar)


NameVar = "Chidera"


def myF():
    global NameVar1
    NameVar = "Johnson"

myF()
print("my name is: " + nameVar)

# NB: if the global keyword is same with the variable your local variable will be called out...
# if the global keyword is not same with the variable your main variable will be called out...

# ==========================================================================================================================
# next class Topic Data Types:
# here we said that python data type are the programmers built-in by default functions that we can use to identify our
# data...

# String - str is for Text
# Numeric Types: int, float, complex
# Mapping Types: dict
# Sequence Types: list, tuple, range...
# Set Types: set, frozenset
# Boolean Type: condition true or false
# Binary Types: bytes, bytearry, memoryview

# Python DataType
"""
this is from the programmers built-in by default functions that we can use to identify our data for accessing

"""
# String - str is for Text n words
# Numberics Types: int, float, double and complex
# Mapping Types: dict
# Sequence Types: List, tuple, range... (object)
# Set Types, set, frozenset
# Boolean Types: contionals true or false
# Binary Types: bytes, bytearry, memoryview

# Casting in python: uses what we call constructor function
"""
int() - is a constructs of an integer number from an integer literal, where a float literal (by removing all decimals), or a string literal(providing the string represents a whole number)

float() - same as above where integer truns to floating number

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literal
"""
# integer
x = int(99) # x will return 99
y = int(99.0) # y will return 99
z = int("3") # z will still return 3 as a number or integer
print(x)
print(y)
print(z)
print(type(z))

# Floats:
X = float(99) # X will return 99.0
Y = float(99.9) # Y will return 99.9
Z = float("3") # Z will return 3.0
W = float("99.9") # W will still return 99.9

#example
a = "10"
A = int("20")
b = 10
B = "20"
c = b + A
print(c) # 30

d = a + B

print('string numbers: ', d) #

# Strings:
xx = str("m1") # xx will return 'm1'
yy = str(99) # yy will be '99'
zz = str(99.9) # zz will return '99.9'

# String Example:
text = "this is text is invovlved about 400 words max "

# Numeric Example:
int_number = 1234567890
float_number = 50.6
complex_num = 1j

# Example for Sequence
list_word = ["car", "house", "money"]
tuple_word = ("car", "house", "money")
range_Number = (8)

# Mapping Type
dict_word = {"Keys": "Values", "Name": "Peter", "Age": 70}

# Set Types Example
set_word = {"car", "marriage", "money"}
frozenset_word = frozenset({"money", "house", "car"})


# Boolean Type Example
On_light = True
Off_light = False

# Binary Types Example:
bytes_number_checking = b"Hello"
bytearray_number_checking = bytearray(8)
memoryview_checking = memoryview(bytes(500))


# Assigning Number
Age = 20
print(Age)
money = 1000.99
print(money)
kelven = 1j
print(kelven)


# checking for the types
print(type(Age)) #number
print(type(money))
print(type(kelven))

# Coverting from one data Type to another: which is called casting method
cov_age_into_float = float(Age)
print(cov_age_into_float)
ft_into_int = int(money)
print(ft_into_int)
float_into_comp = complex(money)
print(float_into_comp)

# Random Number
# 0we need import the python random at the number1 workspace: import random
print(random.randrange(0, 100))

# Next Topic Python String





