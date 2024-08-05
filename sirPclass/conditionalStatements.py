"""
PYTHON CONDITIONAL AND IF STATEMENTS

here we commonly use "if statements" and loops

keyword If: indentation relies also as syntax

where: Equals: a == b
        not Equal: a != b
        less than: a < b
        less than or Equal to: a >= b
        Greater than: a > b
        Greater than or Equal to: a >= b

"""

a = 33
b = 333

# where we have only one condition to check for: we use only IF and return
if b > a:
    print("Yes B is greater than a")

# where we have two or more one condition to check for: we use "if, elif, ... else is also the default

# this elif: will execute if the if condition is not meant

A = 666
B = 666
c = 999
C = 9999

if A != B:
    print("A and B is same")
elif c != C:
    print("c and C are not the same")
else:
    print("Non of the above is True")


# Short hand of IF Statement
if A < c: print('printing for IF Statement', "yes is correct!")

# # Short hand of else Statement

print('printing for Else Statement', "yes is correct!") if C > c else print('printing for Else Statement', "No is not correct!")
print('printing for Else Statement', "yes is correct!") if C < c else print('printing for Else Statement', "No is not correct!")

# where we have multiple else statements on the same line we use Ternary Operators or conditional Expressions

print("Yes correct!") if c > C else print("same") if C != c else print("Not correct!")

# we can also use the AND keyword
if A == C and A != C:
    print("Both condition must be true")
else:
    print("The two statement is not same")

# we can also use OR keyword
if  B == A or C == A:
    print("yea correct pass code")
else:
    print("you're going no where")

"""
NESTED IF STATEMENT
Here you can have if statements inside if statements, as a nested if statement

"""

inec = 100

if inec > 50:
    print("yes is greater")
    if inec > 80:
        print("yes is above 80")
    else:
        print('Nested if statement:', "both either is not correct!")


"""
The PASS Statement
since if statements cannot be empty, but if you for some reason have an if statement with no content, put is the Pass
statement to avoid getting an error...

"""

if C != c:  # returns Error
    pass
