# python Operators

# This operators are used to perform operation on variables and values

print(15 + 8)

# Types of operators
"""
Arithmetic operators
Assignment operators
Comparison operations
Logical operations
Identify operators
Membership operators
Bitwise operators
"""

# Arithmetic operators: are used with numeric values to perform common mathematical operations

# Examples: + - / *

print(450 + 80)
print(62 - 15)
print(72 / 2)
print(5 * 5)

# % modulus is just like remainder
print("========== modulus ==========")
x = 5
y = 2
print(x % y)  # return 1

# ** Exponentiation converting to base 10
a = 2
b = 5
print(a ** b)  # same as 2*2*2*2*2 = 32

# Floor // division rounds the result down to the nearest whole number
c = 15
d = 2
print(c // d)

print('==================== Assignment Operators ========================')
# these are used to assign values to variables
#  =, +=, -=, /=, %=, //=, *=, **=, &=, |=, ^=, >>=, <<=
e = 5
e **= 6
print(e)


print('==================== Comparison Operators ========================')
# it is used to compare two values: it return true or false boolean
# == Equal sign, != Not Equal, > Greater than, < less than, >= Greater than or equal to, <= less than or equal to
f = 6
g = 4
h = "wow"

print('checking if f is equal to g', f == g)  # This returns False b'cos 6 is not of the same type with 4...
print('checking if f not equal to g', f != h)  # 0this returns True b'cos 6 is not equal to wow

# Greater than
print('checking for greater Than', 4 > 5)  # Returns False b'cos 5 is greater

# Less Than
print('checking if f is less than g', f < g)  # Returns False b'cos F is greater than g

# Greater Than or Equal to
print('checking 4 greater or Equal to 5 : ', 4 >= 5)  # Returns False b'cos 4 is not
print('checking 4 greater or Equal to 4 : ', 4 >= 4)  # Returns True b'cos 4 is equal 4
print('checking 4 greater than 4 : ', 4 > 4)  # Returns False b'cos 4 is not greater than 4



# less than or Equal to
print('checking if 4 is less than or Equal to 5: ', 4 <= 5)  # Returns True b'cos 4 is less than 5
print('checking if 4 is less than or Equal to 4: ', 4 <= 4)  # Returns True b'cos 4 is equal sign to 4
print('checking if 4 is less than 4: ', 4 < 4)  # Returns False b'cos 4 is less than 4


print('==================== Logical Operators ========================')
"""
logical operation: they are used to combine conditional statement:
AND && returns True if both statements are true
OR || returns True if one of the statements is true
NOT ! returns a Reverse the result, returns False if the result is true 
"""

j = 5
k = 10

# AND logical: the both must be a true statement for the code execute
print('checking if j and k is same ', j and k)  # Returns b'cos both is same data type
print(not(j > 3 and j < 10))  # since the statements is true then then not reverses it to false
print(j > 3 and j < 10 ) # returns true since the statement is true

# OR logical: once any statement is true then the code will execute
print('checking if j or k is same: ', j or k)  # Returns True b'cos both is same dat type
print('checking for j with k in OR logical', j > k or k > j)

# NOT logical: since the statements is true then then not reverses it to false
print('checking for NOT statement: ', not(j and k))  # Returns false

print('checking for j with k in NOT statement: ', not(j > k and k < j))  # Returns False

# Identity operators...
"""
this is used to compare the objects, not if they are equal, but if they are actually the same object with the same
memory location....
is : keyword returns True if both variables are the same object
is not : Returns True if both variables are not the same object
"""

studentName = ["max", "peter", "obi"]
StudentName = ["obi", "max"]

checkStudent = studentName
print(checkStudent)
print(studentName)
print(checkStudent is studentName) # Returns True b'cos checkStudent is same as studentName
print(studentName is StudentName) # Returns False both is not same
print(StudentName == studentName) # returns False

print(checkStudent is not studentName) # Returns false b'cos not ! reverses the statement

# Membership Operators
"""
This are used to test if a sequence is present in an Object

we use "in" keyword where it returns True if a sequence with the specified value is present in the object
while "not in" keyword returns true if a sequence with the specified value is not present in the object 
"""

print("johnson" in studentName) # returns false b'cos johnson is not in the array
print("john" not in studentName) # returns true b'cos of the not!

# Bitwise operation
"""
This are used to compare(Binary) numbers

which uses:
& AND This sets each bit to 1 if both bits are 1 as same
| Or This sets each bit to 1 if one of two bits is 1
^ XOR This sets each bit to 1 if only one of two bits is 1
~ NOT This sets an inverts in all the bits
<< ZERO FILL LEFT SHIFT This just shift left by pushing zeros in from the right and let the leftmost bits fall off
>> SIGNED RIGHT SHIFT This shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""






