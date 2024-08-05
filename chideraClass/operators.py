# PYTHON OPERATORS

# This Operators are used to perform operation on variables and values.
print(10 + 5)

# Operators are Grouped as follows:
# Arithmetic operators
# Assignment Operation
# Comparison Operation
# Logical operation
# Identity operators
# Membership Operators
# Bitwise operation

# Arithmetic operators: are used with numeric values to perform common mathematical operations
# Example of Arithmetic operators:
#  + - / *
print(450 + 265)
print(1035 - 256)
print(8654 / 5)
print(4 * 6)

# % Modulus is just like remainder
x = 5
y = 2
print(x % y)

# ** Exponentiation converting to base 10
a = 2
b= 5
print(a ** b) # same as 2*2*2*2*2 = 32

# // Floor division rounds the result down to the nearest whole number
c = 15
d = 2
print(c // d)

# Assignment Operation: these are used to assign values to variables
# = , +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
print(c)
e = 5
e += 6
print(e)

f = 5
f &= 3
print(f)

g = 5
g |= 3
print(g)

# Comparison Operation: these ar used to compare two values:
# == Equal sign, != Not Equal, > Greater than, < Less than, >= Greater than or equal to, <= Les than or equal to

h = 6
i = 4
print(h == i)  # this Returns False b'cos 6 is not of the same type with 4 even as 6 will be str type
print(h != y)  # this returns True because 6 is not equal to 4
print(h >= i)  # this returns True b'cos 6 is greater than 4

# Logical operation: these are used to combine conditional statement:
# And this AND returns True is both statements are true
# OR this OR Returns True if one of the statement is true
# NOT this NOt Reverse the result, returns False if the result is true

j = 5
print(not(j > 3 and j < 10))
# print(j > 3 and j < 10)


# Identity operators...
"""
Identity Operators are used to compare the objects, not if they are equal, but if they are actually the same object,
with the same memory location:
is : Returns True if both variables are the same object
is not : Returns True if both variable are not the same object 
"""
k = ["Benz", "Venza", "lexus"]
l = ["Benz", "lexus"]
m = k
print(k)
print(m)
print(k is m)  # Returns True b'cos m is same object as k
print(l is k)  # Returns False b'cos l is not the same objects as k, even if they have the same content but not equal
print(k == l)
# This is false b'cos it demonstrate the different between "is and "==": this comparison returns True b'cos l is equal to k

n = ["Benz", "Venza", "lexus"]
o = ["Benz", "lexus"]

p = n
print(n is not p)  # Returns false b'cos p is the same object as n

# Membership Operators
"""
This Operators are used to test if a sequence is present in an Object:

in : Returns True if a sequence with the specified value is present in the object
not in : Returns True if a sequence with the specified value is not present in the object
"""

q = ["Benz", "Venza", "lexus", "kekee"]

print("kekee" in q)
print("keke" not in q)

# Bitwise operation
"""
This Operators are used to compare(Binary) numbers

is uses:
& AND This sets each bit to 1 if both bits are 1 as same
| OR This sets each bit to 1 if one of two bits is 1
^ XOR This sets each bit to 1 if only one of two bits is 1
~ NOT This sets an Inverts in all the bits
<< ZERO FILL LEFT SHIFT this just shift left by pushing zeros in from the right and let the leftmost bits fall off
>> SIGNED RIGHT SHIFT this shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 
"""