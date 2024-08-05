# Python String Formatters

print("welcome")
print('welcome')

print("i'm balabala")

# String Assign to a variable
name = "cakahal johnson"

# Multiline String
names = ''''''
Names = """
this is a multiline string where you can write as much code or text as we like
"""

print(Names)

# String in Arrays
my_class_name = "java, python, web, js, css"
print(my_class_name[1])
print(my_class_name)

# String in Loop
# by using the keyword in:
for p in "python":
    print(p)

# Checking for String Length
# we use len() function
my_name = "Python, is awesome"
print(len(my_name))

# Checking for a certain phrase or character if its present in a sting, will use the keyword: in
my_db = my_class_name
print(my_db)

print("joy" in my_db)
print("js" in my_db)
# this return a boolean datatype which is true or false


print("================= if function ===========")
if "html" in my_db:
    print("yes, html is present")
else:
    print("NO, Html is not present")

# Checkin with key word: not in
print("Html" not in my_db)

if "csss" not in my_db:
    print("yes, 'csss' is not present")


# Slicing a String
# This get the characters from position position placed and also not included:

print(my_db[0:5])
print(my_db[:5])

# Slice to End
# picking from back, always by leaving out the end index, the range it will go to the end...
# This get the characters from position 2, and all the way to the end
print(my_db[0:])

# Negative Indexing
# This uses negative index to start the slice from the end of the string:
# class work: use this negative indexing to cut out eb from my_db


# string Modification: python sets this built-in methods that you can use a string
# To turn a text to Upper case use the keyword: upper() methods

eg = " Hello, world; python; is awesome "
print(eg.upper())
print(eg.lower())

# Removing whitespace
print(eg.strip())

# Replacing a string we use the keyword: replace
print(eg.replace("Hello", "Hi"))


# Split String
# we use the keyword split() turn a string to sub-string if find an instances of the separator
print(eg.split(";"))

# String Concatenation
# means to combine two strings you can use + operator....

userName = "Cakahal"
lastName = "Johnson"
fullName = "My fullname is: " + userName + " " + lastName
print(fullName.upper())

# string Format
# this means that you cannot combine strings and numbers like:
myAge = 72
yourAge = 102
# coment = "my age is " + myAge + "years"
# print(coment)
comment = "My age is {} years old man"
print(comment.format(myAge))

qty = 5
price = 2000
ram = 500
myOrder = "i want {0} qty of iphone xmax with ram {1} size for {2} dollars"
print(myOrder.format(qty, ram, price))

# Escape Characters
# this is an illegal characters that we use to replace a string format
# list of Escape characters in python:
"""
\' Single Quote
\\ Backslash
\n New Line
\r Carriage Return
\t Tab
\b Backspace
\f Form Feed
\ooo Octal value
#
"""
commment = "learning: \n \tpython is \bawesome once you're \n done with \"python basics\" as a programmer "
print(commment)
"""
capitalize() this converts the first character to upper case
casefold() Coverts string into lowercase00
center() Returns a centered string
count() Returns the number of time a specified value occurs in a string
encode() Returns an encoded version of the string
format() Formats specified values in a string
index() Searches the string for a specified value and returns the position of where it was found
split() Splits the string at the specified separator, and returns a list
translate() Returns a translated string
strip() Returns a trimmed version of the string

"""
