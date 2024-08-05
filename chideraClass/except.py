"""
Exception Handling
This helps us to know when an error occurs, or exception as in Python or other programming language uses this exception
 to stop your not to generate an error and also generate an error message

 These Exception has Three sections which is the TRY BLOCK this try block lets you test a block of code for errors
    The Except Block: which handles the errors
    Then we have the Finally Block: this lets you to execute code, regardless of the result of the TRY and Except Block

Example: This example we TRY this line an generate an error, because we use X which is not defined:

"""
try:
    print(x)
except:
    print("An exception occured") #outpu: this will hits an error b'cos an X is not defined

# where we have many block of code that we want to check for
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong") #output: The Try block will generate a NameError, because x is not define:


# Here we use the Else keyword to define a block of code to be executed if no errors were raised

try:
    print("Hello Chidera")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong") #Output: The Try block does not raise any errors, so the else block is executed:


# Finally Block: is specified, which we be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("the 'try except' is finished ")


# Exception when we want to open a file in our project
try:
    f = open("demofile.txt")
    f.write("here is the content of the file")
except:
    print("Something went wrong when writting to the file")
finally:
    f.close() #The program can continue, without leaving the file object Open


# these Exception is when you want to throw an exception if a condition occurs
# To throw (or raise) and Exception, use the keyword raise...

x = -1
if x < 0:
    raise Exception ("Sorry, no numbers below zero") # An error will occur

n = "Hello Chidera"
if not type(n) is int:
    raise TypeError("only integers are allowed")
