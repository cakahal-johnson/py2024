"""
Python Operators are the constructs which can manipulates the values of the operands
Types of Python Operators:
Arithmetic Operators
Assignment Operators
Comparisons Operators
Logical Operators
Indentity Operators
Membership Operators
Bitwise Operators

"""

# Arithmetic Operator
"""
basics operands: + - * / 
% as Modulus
** as Exponent
// as Floor Divisions where everything is at floor just as the name

"""
a = 22
b = 10
#  Examples of Addition:
print("a + b ", a+b) # returns 31

#  Examples of Subtraction:
print("a - b : ", a - b)

#  Examples of Multiplication:
print("a x b : ", a * b)

#  Examples of division:
print("a / b : ", a / b)

#  Examples of Modulus returns the remainder after division:
print("a % b : ", a % b)

#  Examples of Exponent means Base10:
print("a Exponent b : ", a ** b)

#  Examples of Floor Division:
print("a // b : ", a // b)

# Assignment Operators:
"""
these is used to assign values to variables most explined with functions and Loops
Example:
= as Equal means re-assigning a value
+= as +ing a value to an existing value
-= as -ing a value to an existing value
*= as *ing a value to an existing value
/= as /ing a value to an existing value
%= as % a value to an existing value
//= as // a value to an existing value
**= as ** a value to an existing value
&= as Bitwise AND
|= as Bitwise OR
^= as Bitwise XOR
>>= as Greater than equal 
<<= as Lessthan equal

"""

print(b) # returns 10

# Re-Assigning a value
c = 2
d = c
print("where c is 2 then c is reassigned to d:", d)

# += as +ing a value to an existing value same as + - * / % ** //
d += 8
print('d is 2 then add to 8:', d) # returns 10

# &= as &ing a value to an existing value

e = 5
e &= 3
print(e) # this returns 1

f = 5
f |= 3
print(f) # returns 7

"""
 Comparison Operators is used to compare the values on either sides of them and
decide the relations among them, you can also call them Relational Operators

where it returns Booleans which is True or False

Examples: since is conditionals it checks Equalities
== Equal TO ass dataType
!= as Not Equal
> Greater Than
< Less Than
<= Less Than n Equal
>= Greater Than n Equal


"""

# Equal TO
print(4 == 4) # returns True
print(4 == 5) # returns False

# Not != Equal
print(4 != 5) # Returns True

# Greater Than >
print(4 > 5) # returns False

# Less Than >
print(4 < 5) # returns True

# Greater Than > n Equal To
print(4 >= 5) # returns False
print('is 4 > 4 ?: ', 4 > 4) # returns ? False
print('is 4 >= 4 ?: ', 4 >= 4) # returns ? True










