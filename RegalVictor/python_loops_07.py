"""
PYTHON CONDITIONAL AND IF STATEMENTS

WHERE: Equals a == b
       Not equal a != b
       less than a < b
       less than or equal a <= b
       great than or equal a >= b
"""

"""
PYTHON LOOPS
This is also python primitive datatype

while loops
for loops

where: WHILE loop we can execute a set of statements as long as a condition is true it keeps loop (i.e is good for int values)

       FOR LOOPs is used for iterating over a sequence(i.e either a list, a tuple, a dictionary, a set, or a string)
       with the FOR loops we can execute a set of statements, once for each item in a list, tuple, set...
"""
print("while loops")

# syntax:
i = 1
while i < 11:
    print(i)
    i += 1

print("this increment i is very important, or else the loop will continue forever")

# The Break Statement: we can use Break statement to stop the loop even if the while condition is true
n = 0
while n < 6:
    print(n)
    if n == 4:
        break
    n += 1

# the continue statements: where we stopped the current iteration and now want to continue with the next loops
print("continue statements")
a = 0
while a < 6:
    a += 1
    if a == 3:
        continue
    print(a)


# The Else statement where we can run a block of code once or when the condition no longer true
print("Else statements")
b = 1
while b < 6:
    print(b)
    b += 1
else:
    print(" B is no longer less that 6")


print("===================FOR LOOPs============================")
course = ["Java", "Python", "Php"]
for z in course:
    print(z)

# this for loops dose not required an indexing variables to set beforehand

for c in "python":
    print('here is for loop for python', c)

#  using Break Statements for FOR LOOPs
Course = ["html", "css", "bootstrap", "javascript"]
for d in Course:
    print(d)
    if d == "bootstrap":
        break

# another syntax for break
web = ["html", "css", "bootstrap", "javascript"]
for e in web:
    if e == "css":
        break
    print('another break: ', e)


#  Continue Statement for FOR LOOPs
Web = ["html", "css", "bootstrap", "javascript", "Php"]
for f in Web:
    if f == "bootstrap":
        continue
    print(f)

for f in Web:
    if f == "bootstrap":
        continue
    print(f)


print("=================== python Range ========================")
"""
This function returns a sequence of numbers starting from 0 by default, and increments by 1(by default), and ends a 
specified number
"""

for g in range(10):
    print('print for Range', g)

#  Range with 2 params starts and end
for j in range(5, 16):
    print(j)


# Range with 3 params where the 3rd is the increment(the last fig)

for k in range(2, 30, 3):
    print('Range with 3 params: ', k)


# Else in FOR LOOPs

for l in range(8):
    print(l)
else:
    print("finally finished!!")
    
    
#  else block will not be executed if the loop is stopped by a break statement
for o in range(9):
    if o == 4:
        print(o)
    else:
        print("Finally Finished!!!")

print("=========================== Python Nested Loops ==========================")
"""
A Nested Loops is a Loop inside a Loop
where: the Inner Loop will be executed one time for each iteration of the Outer Loops 
"""

abc = ['A', 'B', 'C', 'D']
num = [1, 2, 3, 4]

for an in abc:
    for na in num:
        print(an, na)


print("case difference")
lowerr = ['a', 'b', 'c']
uppper = ['A', 'B', 'C']

for ll in lowerr:
    for up in uppper:
        print(ll, up)


# We use Pass in FOR LOOP just to avoid getting an error
for p in [0, 1, 2, 3]:
    pass