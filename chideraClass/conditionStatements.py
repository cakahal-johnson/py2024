"""
PYTHON CONDITIONS AND IF STATEMENTS

NB: we should know that python supports the usual logical conditions from mathematics.
    These are commonly in "if statements" and loops.
    An "if statement" is written by using the IF keyword

    Indentation also relies on these which the (whitespace at the beginning of a line)

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or Equal to: a <= b
    Greater than: a > b
    Greater than or Equal to: a >= b

"""

# Examples:

# a = 33
# b = 256
# if b > a:
#     print("b is greater than a")

# elif: means what happens when our first line code is not executed than the elif will be check next
# by using the keyword elif
# c = 555
# d = 555
# c = 100
# if d > c:
#     print("d is greater than c")
# elif c == d:
#     print("c and d are equal")
# elif d < c:
#     print("Yes d is greater c")

print("here we use if, elif, else")
# x = 200
# y = 66
# if y > x:
#     print("y is Greater than x")
# elif y == x:
#     print("Yes y and x are equal")
# else:
#     print("x is Greater than y")

# a = 35
# b = 3225
# print("A")if a > b else print("B")

# a = 888
# b = 888
# print("A") if a > b else print("=") if a == b else print("B")

# this shorthand can also have an And sign
# a = 854
# b = 66
# c = 500
# if a > b and c < a:
#     print("both conditions are True")


# NESTED IF: is when you have a if statement inside another if statement
#
# x = 41
# if x > 10:
#     print("i'm Above 10")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20")


#  THE PASS STATEMENT
#  IF statements cannot be empty, but if you have some reason to then the if statement with no content, put in the pass
#  statement to avoid getting error.
#
# a = 55
# b = 352
#
# if b > a:
#     pass

# having an empty if statement like this, would raise an error without the pass statement...


"""
PYTHON LOOPS
It has two primitive loops commands:
--- while loops
--- for loops

---while loop execute a set of statements as long as a condition
"""

# i = 1
# while i < 10:
#     print(i)
#     i += 1

    # With the BREAK STATEMENT: we can stop the loop even if the while condition is true:

# i = 1
# # while i < 100:
# #     print(i)
# #     if i == 50:
# #         break
# #     i += 1
# #
# # i = 1
# # while i < 100:
# #     print(i)
# #     if i == -50:
# #         break
# #     i -= 1

#  with CONTINUE STATEMENT we can stop the current iteration, and continue with the next:

# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

#     Note that the 5 will be missing in the result


# It has a ELSE STATEMENT we can run a block of code once when the condition no longer is ture

# i = 1
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 10 ")

# classwork
# i = 1
# while i < 20:
#     print(i)
#     i += 1

"""
PYTHON FOR LOOP
a FOR loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string.

this is less like the for keyword in other programming languages, and works more like an iterator method as found in other
object-orientated programming languages.

with the FOR loop we can execute a set of statements, once for each item in a list, tuple, set etc....
"""

# cars = ["benz", "lexuz", "toyota", "bus"]
# for x in cars:
#     print(x)

# for a in "banana":
#     print(a)

# BREAK STATEMENT FOR LOOPS

# cars = ["benz", "lexuz", "toyota", "bus"]
# for x in cars:
#     print(x)
#     if x == "toyota":
#         break

# cars = ["benz", "lexuz", "toyota", "bus"]
# for x in cars:
#     if x == "toyota":
#         break
#     print(x)

# CONTINUE STATEMENT FOR LOOPS
# with the CONTINUE loop statements we can stop the current iteration of the loop, and continue with the next

# cars = ["benz", "lexuz", "toyota", "bus"]
# for x in cars:
#     if x == "toyota":
#         continue
#     print(x)

"""
THE RANGE() FUNCTION
To loop through a set of code a specified number of times, we can use the range() function

the range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default)
and ends at a specified number.

"""

# for x in range(100):
#     print(x)

# for x in range(2, 50):
#     print(x)


#  RANGE INCREMENT SEQUENCE is by having 3 parameters...
# for x in range(2, 30, 3):
#     print(x)

# HERE WE USE THE ELSE THE PRINT OUT MESSAGES
# for x in range(30):
#     print(x)
# else:
#     print("Finally finished what we have in the iteration")

# Nb: the else block will not be executed if the loop is stopped by a break statement

# for range BREAK
# for x in range(30):
#     if x == 22: break
#     print(x)
# else:
#     print("Finally finished what we have in the iteration")

"""
NESTED LOOPS
A nested loops is a loop inside a loop.
the "inner loop" will be executed one time for each iteration of the "outer loop"
"""
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in fruits:
#         print(x,y)

# THE PASS STATEMENTS
# FOR loop cannot be empty, but if you for some reason have a FOR loop with no content, put in the pass
# statement to avoid getting an error
#
# for x in [0,1,2]:
#     pass
