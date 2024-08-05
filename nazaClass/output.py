import random

print("cakaha johnson")

# comments crlt / single line comments


"""
This section is a multiline comments
kjsksks
ksksksk
sksksk

"""

# Variable is a container for storing data values...

# multiline Strings
To_day_topic = """
python java css html javascript \npython java css html javascript \n python java css html javascript \npython java css html javascript
\tpython java css html javascript
python java css html javascript

"""
print(To_day_topic)

Global_Keyword = """
When creating a variable inside a function it's a 'local variable' which can only be used inside that function
but to create a global variable inside a function we have to use the Keyword "Global"
"""
print(Global_Keyword)

def myName():
    global MyName
    MyName = "cakahal johnson"

myName()
# print(MyName)
print("my name is " +MyName)
print("you can call me " +MyName)
print("i love to be called by" +MyName)
print(MyName+ " love python")

glo ="""
if the global keyword is same with the variable your local variable will be called out...
then if the global keyword is not same with the variable your main variable will be called out
"""
print(glo)

my_Name = "cakahal"


def myFnc():
    global my_Name1
    my_Name = "Johnson"


myFnc()
print(my_Name)


# PYTHON DATA TYPES
# We that python Data types are the programmers built-in by default functions that we can use to identify our data

# String: list, tuple, (map) dic (dictionaries)
list_word = ["car", "house", "money"]
tuple_word = ("car", "house", "money")
dic_word = {"name": "Naza", "Age": 70}  # mapping
String_word = "money"
range_number = (6)  # Sequence

# SET TYPES: set, frozenset
# Example:
set_word = {"house", "car", "shop"}
frozenset_keyword = frozenset({"money", "house", "car"})

# just get the different of above strings

# Boolean Type: bool which setting a condition to True or false
#Example:
ON_light = True
Off_light = False

# Binary TYPES: bytes, bytearry, memoryview
#Example
bytes_checking = b"Hello"
print(bytes(b"hello")) # this has to be in function or inside a memoryview
bytearray_checking_keyword = bytearray(9)
print(bytearray(9))
memoryview_checking = memoryview(bytes(500))

# Number TYPES:
int
float
complex

# Assigning
int_Age = 80
float_money = 100.30
complex_kelven = 1j

# we said that type() is used to check class names
print(type(int_Age))

# converting from one form to another: which is also called casting method
cov_age_int_into_float = float(int_Age)  # we use keyword float then cast in the parameter which we want to check
cov_money_float_into_int = int(float_money)
cov_kelven_complex_into_float = complex(float_money)
complex_kelevn_into_int = complex(int_Age)

print(int_Age)
print(cov_age_int_into_float)


print(random.randrange(0, 99))

# String Format
# single and multiline strings

# Strings in Arrays
# NB: first of an array is 0
NAME = "Naza", "Cakahal", "Johnson", "Doe", "cat"
print(NAME[-0])

print("============================== loop starts =======================")
# Strings in loop
for f in "cakahal":
    print(f)
else:
    print("nnnn")

print("============================== loop ends =======================")

# checking for string Length
# we use the len() keyword
print(len(NAME))

# checking for a certain phrase or character if its present in a string, we use the keyword: in
print("dog" in NAME)

if "Doe" in NAME:
    print("Yes Joy is present")
else:
    print("No JOY is absent")


# checking with keyword: not in
print("johnson" not in NAME ) # this returns Boolean

if "mark" not in NAME:
    print("Yes mark is present")
else:
    print("mark is absent")

# Slicing a String
# This gets the characters from position placed and also not included:
print(NAME[0:5]) # b'cos name var are strings not arrays

students = "Cakahal, johnson, Doe, Naza, Joy"
print(students[0:1])
print(students[:7])

# 0: means slice to the end
# picking from back, always by leaving out the end index, the range it will go to the end...
# start and stop

# Negative Indexing
# This use negative index the start the slice from the end of the string
print(students[]) # return za
