print('welcome')
# variables
# data types
# opt
# conditionals
# functions
# loops

import random
x, y, z = 11, 38.32, 1j

a = random.randrange(1, 100)

name = "my name is chinonso, i am {} yrs old"
print(name.format(a))

my_student = [0, 33, 43, 33]
print(my_student)

my_student[2] = 21
print(my_student)

#************list********as in Arry in Js***************
# numerical index, can store duplicate value, created w/[], changeable

mylist = [ 'apple', 'banana', 'cherry']
mylist[2] = 'mango'
print(type(mylist))

#tuple
# ordered, created w/(), immutable, allow duplicate
mytub = ('apple', 'banana', 'cherry')

print(mytub)
# mytup[2] = 'strawberry'

print('cherry' in mytub)

(frt1, frt2, frt3) = mylist
print(frt3)

#set
# unordered, created w/{}, unchangeable, dose not allow duplicate value

myset = {'apple', 'mango', 'cherry'}
#print(myset[1])

#dictionary
#ordered, mutable, does not allows duplicate values, created w/{}, it has kays and values

mydic ={
    'std1': 'chinonso',
    'std2': 'chinaza',
    'std3': 'chelsea',
}

print(mydic['std2'])

#while loop*************

i = 1
while i < 5:
    print(i)
    i += 1

for x in range(5):
    print(x)

#for loop***********
#any str data is seen as an aryay



