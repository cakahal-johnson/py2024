"""
PYTHON BOOLEANS
Booleans represents one of two values: True or False

this can used where you often need to know if an expression is True or False.
also where you want to evaluate any expresion in python, and get one of two answers, True or False
also where you want to compare two values, the expression is evaluated and python returns the Boolean answer

"""

# using Booleans in operators
print(10 > 9)
print(10 < 9)
print(10 == 9)
print(10 != 9)

# using boolean in function
a = 200
b = 199

if b > a:
    print("Yes B is greater than A")
else:
    print("NO B is not greater than A")

# using Booleans to evaluate values and variable
# here using Booleans as a function methods we use bool() function which allows you to evaluate any value,
# and give you True or False in return,

print(bool("My name is Chidera"))
print(bool(15))

# Evaluating two variables:
x = "I'm chidera"
yr = 70

print(bool(x))
print(bool(yr))


"""
Almost any value is evaluated to True if it has some sort of content
Any string is True, except empty string.
Any number is True, except 0.
Any list, tuple, set and dictionary are True, except empty ones...
"""
print("here i will be print below ")
print(bool("abc"))
print(bool(""))
print(bool(123))
print(bool(0))
print(bool(["apple", "cherry", "banana"]))
print("list below")
print(bool([]))


"""
One more value, or Object in this case, evaluates to False, and that is if you have an object that is made from a
class with a __len__ function that returns 0 or False as in OOP class
"""


class MyClass:
    def __len__(self):
        return 0


myJob = MyClass()
print(bool(myJob))


