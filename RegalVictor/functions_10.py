"""
PYTHON FUNCTIONS
function is just a block of code which only runs when it is called out.
--it can also be a Data, known *args is a parameter which accepts an argument
-- A function can return a Data as a result

Syntax:
Creating a function:
we use the keyword "def" means defining

NB: when an information is passed into function it's an Arguments

Arguments:
    Is specified after the function name, inside the parentheses. You can add as many args as you want just separate
     with comma

     NB: if you try to call function with 1 or 3 args, without matching it with the call out function you will basically
      get an error

      Arbitrary Arguments, *agrs
      if you do not know know how many argument that will be passed into your function, just add a * before the parameter
      name in the function definition this is best when handing tuples

      *Arbitrary Keyword Arguments, **kwargs
      same as *args but best for dict

"""

# Function Syntax
def my_func():
    print("python is awesome")

# here we call out the function
my_func()
my_func()
my_func()
my_func()

# Function with an Argument
def my_Func(firstname):
    print(firstname + " Cakahal")

my_Func("Johnson ")
my_Func("Obi ")
my_Func("Regal")

# Function with two Argument
def my_two_func(fname, lname):
    print("welcome to python class: " +fname+ " " + lname)

my_two_func("cakahal", "johnson")
my_two_func("peter", "obi")
my_two_func("Regal", "Victor")

# Arbitrary Arguments. *args
def my_Abi_agrs(*ppl):
    print("How many ppl loves python " + ppl[2] )

my_Abi_agrs("cakahal", "johnson", "Victor", "Regal", "Obi")

# we can use keywords as Args, in this case the order does not metter
def my_key(java2, c1, py3):
    print("The best computer programming lang is: "+ py3 +" Or: " +c1)

my_key(py3="AI, App", java2="android", c1="gaming")

# double Arbitrary Keyword
def my_D_Abi(**kid):
    print("The last Login name is: " + kid["fname"])

my_D_Abi(fname= "Obi", lname="peter")

# Using a Default Parameter Value
def myDF(country="Biafra"):
    print("I am a from: "+ country)

myDF("London")
myDF("")
myDF()
myDF("Nigeria")


# here using a List as an argument
def myList(courses):
    for x in courses:
        print(x)

courses = ["Python", "java", "c++", "c#"]
car = ["benz", "lexus", "venza"]

myList(courses)
myList(car)

# int section

# Using Return Statement

def myRS(a):
    return  5 + a

print(myRS(8))
print(myRS(100))
print(myRS(5))


# Using Return with Args
def myRSA(n, m):
    return n + m

print(myRSA(22, 4))

# using the PASS Statement: b'cos a function definitions cannot be empty, so we the pass statement to avoid getting an error

def MyPass():
    pass

print("RECURSION")
"""
python Recursion means: a defined function that can call itself
is common with mathematical and programming concept. that benefit loop through a data to reach a result which is easy 
to slit into functions 

"""

def my_rec(k):
    if(k > 0):
        result = k + my_rec(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n \nRecursion Examples Results")
my_rec(2)

"""
in this example: my_rec is a function that we have defined to call itself(recurse). we use the k var as the data
which decrements(-1) every time we recurse, so the recursion ends when the condition is not greater than 0(i.e when is 0)

"""

# printing a christmas tree pathern
# def triShape(v):
#     for i in range(v):
#         for j in range(v-i):
#             print(' ', end=' ')
#         for p in range(2*i+1):
#             print('*', end=' ')
#         print()
#
# # generating the pole shape for the tree
# def poleShape(v):
#     for i in range(v):
#         for j in range(v -1):
#             print(' ', end=' ')
#         print('* * *')
#
# row = int(input('Enter a Number of Rows: '))
#
# triShape(row)
# triShape(row)
# poleShape(row)


# creating a time glass pattern
# here we start with Reading or entering the rows
# row = int(input("Enter number of Rows: "))

# Strings in recursion
# checking for vowel or consonant using Function
def checkVowel(u):
    if(w >= 'a' and w <= 'z') or (w >= 'A' and w <= 'Z'):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if w in vowels:
            return 1
        else:
            return 2

print(end="Enter a Character: ")
w = input()

size = len(w)
if size > 1:
    print("\n Invalid Input!")
else:
    chk = checkVowel(w)
    if chk == 1:
        print("\n You pick a Vowel")
    elif chk == 2:
        print("\n You picked a consonant")
    else:
        print("\n You picked Neither Vowel or Consonant")
