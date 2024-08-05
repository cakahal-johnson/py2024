import random

print("Hello Chidera")
#
# if 2 < 5:
#     print("Yes im the comment section is greater than 2")

#  crt / key is for python comment key, which means that the content will not run out!

# for multiline comments

"""
this section is commented out

"""
if 5 > 2:
    print("5 is greater than 2")
if 5 > 2:
    print("5 is less than 2")

#     Python Variables
"""
Variables are containers for storing data values...

# these are legal ways of assigning a variable
    camel-case, pascal-case, snake-case, Upper-case, word-and-number
    # myVar, my_var, MyVar, MYVAR, myvar2

# these are illegal way of assigning variables 
    number-before-word, using a - , using a white-space...
    # 2myvar, my-var, my var....

"""

x = 5
y = "Johnson Variables are containers for storing data values these are illegal way of assigning variables"
print(x)
print(y)

print("chidera")
print(y)
print(y)
print(y)

# Casting... if you want to specify the data type of a variable, this can be done with casting...

word = str(3)
number = int(3)
dic = float(3)

print(dic)
print(number)
print(word)

# GETTING THE DATA TYPE
print(type(word))
print(type(dic))
print(type(number))

# Many Values to Multiple Variables
# python allows you to assign to multiple Variables in one line:

print("HERE IS WHERE OUR CLASS STARTS TODAY")

a, b, c = "Orange", "car", "Mango"

print(b)
print(a)
print(c)

d = e = f = "Ball"
print(d)
print(e)
print(f)

car = ["benz", "lexus", "venza"]

n, m, g = car
print(m)
print(n)
print(g)


# Output Variables
# since print statement is often used to output variables, then to combine both text and a variable,
# we use: + character:

name = "Chidera"
name2 = "Cakahal"
print(x)
print("My name is "+ name +" and also with "+ name2)
print("python is awesome.....")

name3 = "Python is "
name4 = "awesome"
name5 = name3 + name4
print(name5)

add = 522
add2 = 50
print(add + add2)

add3 = 522
add4 = "chidera"
# print(add3 + add4) // this will hit error because is of two different type of DATA TYPE Values

# GLOBAL KEYWORD
# When you create a variable inside a function, that variable is local, and can only be used inside that function
# To create a global variable inside a Function, you can use the global keyword

def myName():
    global z
    z = "Chidera"

myName()
print(z)
print("my Name is "+z)
print("my Name is "+z)
print("my Name is "+z)

# this prints out the local variable b/c it is using the global Keyword
MyName = "Cakahal Johnson"

def Myfunc():
    # this is the local variable
    global MyName
    MyName = "Cakahal"

Myfunc()
print("my Name is " + MyName)

# this prints out the Global variable b/c it is using a d/f global keyword

# this is the global keyword
MyName = "Cakahal Johnson"

def Myfunc():
    # this is the local global keyword
    global MyName1
    MyName = "Cakahal"

Myfunc()
print("my Name is " + MyName)

# NB: if the global keyword is same with the variable your local variable will be called out...
#     if the global keyword is not same with the variable your main variable will be called out...

# Next Topic DATA TYPES

# Types Of Python Data Types
# we said that Python Data Types are the programmers built-in by default functions that we can use to identify our data
# in a different categories:

# Text Type: str (as in String)
# Example:
text = "i'm used when even text is 400 involved in my function. "

# Numeric Types: int, float, complex
# Example:
int_number = 1234567890
float_number = 50.2
complex_number = 1j

# Sequence Types: list, tuple, range
# Example:
list_word = ["car", "house", "money"]
tuple_word = ("car", "house", "money")
range_Number = (6)
# print(range_Number)

# Mapping Types: dict
# Example:
dictionaries = {"Name": "Chidera", "Age": 70}

# Set Types: set, frozenset
# Example:
set_word = {"house", "marriage", "money"}
frozenset_word = frozenset({"money", "house", "car"})

# Boolean Type: bool
# Example:
ON_light = True
Off_light = False

# Binary Types: bytes, bytearry, memoryview
# Example:
bytes_checking = b"Hello"
bytearray_checking = bytearray(6)
memoryview_cheching = memoryview(bytes(500))


# Python is of Three Types:
# Types
int
float
complex

# Assigning
int_age = 80
float_money = 100.99
complex_kelven = 1j

# checking for the types
print("Here is for knowing the assigned number data type above")
print(type(int_age))
print(type(float_money))
print(type(complex_kelven))

# converting from one form to another: which is as a casting method
age_Int_into_float = float(int_age)
money_Float_into_Int = int(float_money)
kelven_complex_into_float = complex(float_money)
complex_kelven_cov = complex(int_age)

print("Here is for printing put their values")
print(int_age)
print(float_money)
print(float_money)

print("Here is for converting numbers to different number data type")
print(age_Int_into_float)
print(money_Float_into_Int)
print(kelven_complex_into_float)
print(complex_kelven_cov)

print("print out 1j into 10.0")
our_1j = 10
ans = float(our_1j)
print(ans)

# Python Random Number
# to use python Random Number
# we have to import the python the random number at the top of our project: import random
print("Here we print random values of different types when ever we re-run this app")
print(random.randrange(0, 1000000000000000))

# next Topic Python Strings
# things we should know about python string

print("Welcome")
print('Welcome')

# How to assign String to a Variable
hi = "You are Welcome"
print(hi)

# Multiline Strings
Hi = """here is a multiline string 
format as we use this to list out a multiline text
which can also starts with a single quotation mark ''' content here ''' 
"""
print(Hi)

# Strings in Arrays
HI = "my, name, is, chidera, i'm, learning, python"
print(HI[1])

# String in Loop
for f in "Banana":
    print(f)

# Checking for String Length
# to ye the of a string, use the len() function
hI = "Python, is, Awesome"
print(len(hI))

# checking for a certain phrase or character if its present in a string, will use the word: in.

my_db = "Chidera, cakahal, mark, joy, johnson"
print("jane" in my_db)
print("joy" in my_db)

my_DB = "Chidera, cakahal, mark, joy, johnson"
if "joy" in my_DB:
    print("Yes, 'joy' she is present. ")

# checkin with key word: not in
My_db = "Chidera, cakahal, mark, joy, johnson"
print("johnson" not in My_db)

if "mark" not in My_db:
    print("yes, 'mark' is NOt present ")


# Slicing a String
# This get the characters from position placed and also not included:

print(My_db[0:7])
print(My_db[:7])


# Slice To thh End
# picking from back, always By leaving out the end index, the range it will go to the end...
# This get the characters from position 2, and all the way to the end:
print(My_db[0:])


# Negative Indexing
# This uses negative indexes tro start the slice from the end of the string:
# Lets get character: son
print(My_db[-3:])


# String Modification: python sets this built-in methods that you can use on strings.
# To Upper Case uses the keyword: upper() methods

eg = " Hello, Chidera "
print(eg.upper())
print(eg.lower())

# Removing whitespace
print(eg.strip())

# Replacing a String wth the keyword word replace
print(eg.replace("Hello", "hi"))

# Split String
# with the keyword: split() method splits the string into substings if iot finds instances of the separator:
print(eg.split(","))


# next class String Concatenation
# String Concatenation
# To Concatenate, or Combine, two strings you can use + operator....
k = "You are late "
l = "i think we should change the timetable"
p = k + l
print(p)

o = k + " " + l
print(o)

# String Format
# this means that you cannot combine strings and numbers like this:
mAge = 70
Nage = 100
# comment = "Nigeria is a " + mAge + "Years old man"
Comment = "Nigeria is {} Years old man"
# print(comment)
# so to solve this error we use a .format() method to insert numbers into string while we use {} catch the variable:
print(Comment.format(Nage))

Quantity = 5
ram = 128
price = 1.2
MyOrder = "I want {2} iphone 13 pro max with a ram {0} size for {1} million"
print(MyOrder.format(Quantity, ram, price))


# Escape Characters
# to insert characters that are illegal in a string, we use an escape characters.
# An escape character starts with \ backslash followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# exmple:
# badTXT = "this we hit an Error bcos it also have a double "Quotes" inside a string quotes"
# To correct above error:
goodTXT = "learning python is awesome once you're done with \"python basics\" as a programmer "
# list of Escape Characters in python: \' Single Quote
#                                      \\ Backslash
#                                       \n New Line
#                                       \r Carriage Return
#                                       \t Tab
#                                       \b Backspace
#                                       \f Form Feed
#                                       \ooo Octal value
#                                       \xhh Hex value

# String Methods
# This strings methods is a set of built-in methods that you can use on strings.
# NB: all string methods returns new values. they do not change the original string...

cap = "here we this to be in capitalize methods"
# c = cap.capitalize()
c = cap.upper()
print(c)

"""
capitalize() this converts the first character to upper case
casefold() Coverts string into lowercase
center() Returns a centered string
count() Returns the number of time a specified value occurs in a string
encode() Returns an encoded version of the string
format() Formats specified values in a string
index() Searches the string for a specified value and returns the position of where it was found
split() Splits the string at the specified separator, and returns a list
translate() Returns a translated string
strip() Returns a trimmed version of the string

"""






