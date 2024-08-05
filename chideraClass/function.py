"""
PYTHON FUNCTIONS
A function is a block of code which only runs when it is called
You can pass data, known as parameters, into function.
A function can return data as a result.

CREATING A FUNCTION
In python a function is defined using the def keyword:

NB: Informations can be passed into function as ARGUMENTS
ARGUMENTS:
    are specified after the function name, inside the parentheses. You can add as many arguments as you want,
    just separate them with a comma.

NB: if you try to call function with 1 or 3 arguments, without matching it with the call out function you will basically
    get an error

    Arbitrary Arguments. *args
    if you do not know how many argument that will be passed into your function, add a * before the parameter name
    in the function definition this is best when handling tuples

    *Arbitrary Keyword Arguments, **kwargs
    : same as *args but best for dict, dictionary

"""

# calling out functions
# def my_function():
#     print("Python is awesome")
#
#
# my_function()
# my_function()
# my_function()

# having an Arguments as a parameters
# def my_surname(fname, lname):
#     print(fname + " " +lname)
#
#
# my_surname("Johnson", "Cakahal")
# my_surname("Chidera", "Obident")

# For *args and **kwargs
# def my_cars(*cars):
#     print("My best car is " +cars[2])


# my_cars("benz", "Glk", "Lexus")

# def My_cars(benz, lexus, tayota):
#     print("My best car is " +benz +lexus +tayota)

# My_cars(benz="benz", lexus=" Glk", tayota=" Lexus")


# Using a parameter function'
# def my_fun(country = "London"):
#     print("I am from " +country)
#
#
# my_fun("Sweden")
# my_fun("USA")
# my_fun()
# my_fun("Nig")

# List as a Arguments
# def my_list(food):
#     for x in food:
#         print(x)
#
#
# fruits = ["apple", "banana", "berries"]
#
# my_list(fruits)


# Returning a Value function
# def my_R(x):
#     return 5 * x
#
# print(my_R(8))
# print(my_R(2))


# Pass Statement
# b'cos functions definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statements to avoid getting an error

# def my_functio():
# #     pass

"""
RECURSION 
Python also accepts function recursion, which means a define function can also call itself
"""

# def my_recur(k):
#     if(k > 0):
#         result = k + my_recur(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
# print("\n \nRecursion Results")
# my_recur(6)


# Christmas Tree Pathern
def triangleShape(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*', end=' ')
        print()


# Generating pole shape
def poleShape(n):
    for i in range(n-1):
        for j in range(n - 1):
            print(' ', end=' ')
        print('* * *')


row = int(input('Enter Number of the Rows: '))

triangleShape(row)
triangleShape(row)

poleShape(row)