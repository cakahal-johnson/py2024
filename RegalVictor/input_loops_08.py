import calendar
"""
Python Inputs
in version 2.7 where using raw_input()
while 3.6 is using input()

"""

username = input("Enter Your Username")
print("Welcome to your Dashboard: " + username)

# checking for or if Vowel or Consonant is presents
#
# print("Enter the Character: ")
# ck = input()
#
# # here we pass the conditions
# if ck == 'a' or ck == 'e' or ck == 'i' or ck == 'o' or ck == 'u':
#     print("\n Your Input is a Vowel")
# elif ck == 'A' or ck == 'E' or ck == 'I' or ck == 'O' or ck == 'U':
#     print("\n Your Input is a Vowel")
# else:
#     print("\n Opps it's a Consonant")
#
#
# # here we len() method we also use nested if statement
# print(end="Enter a Character: ")
# chk = input()
#
# size = len(chk)
#
# if size > 1:
#     print("\n Invalid Input")
# else:
#     if( chk >= 'a' and chk <= 'z') or (chk >= 'A' and chk <= 'Z'):
#         if ck == 'a' or ck == 'e' or ck == 'i' or ck == 'o' or ck == 'u':
#             print("\n\"" +chk+  "\" Your Input is a Vowel")
#         elif ck == 'A' or ck == 'E' or ck == 'I' or ck == 'O' or ck == 'U':
#             print("\n\"" +chk+  "\" Your Input is a Vowel")
#         else:
#             print("\n\"" +chk+  "\" Your Input is a Consonant")
#
#     else:
#         print("\n\"" + chk + "\" Your Input is neither a Vowel or a Consonant")
#
#
# # we use len() with lesser code format holding the vowels in a local variable
# print(end="Enter a Character: ")
# chck = input()
#
# size = len(chck)
# if size > 1:
#     print("\n Invalid Input")
# else:
#     if (chck >= 'a' and chck <= 'z') or (chck >= 'A' and chck <= 'Z'):
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         if chck in vowels:
#             print("\n\"" +chck+ "\" is a Vowel")
#         else:
#             print("\n\"" +chck+ "\" is a Consonant")
#     else:
#         print("\n\"" +chck+ "\" is neither a Vowel or a Consonant")
#
#
#
# Here we will Int for the Input() method using FOR loop and range

# TimeTables
# print(end="Enter a number: ")
# num = int(input())  # int makes it just a number only
#
# no = 1
# print("\n Multiplication Table: ")
# for i in range(10):
#     num1 = num * no
#     print(num1)
#     num = num+1
#
#
# # Second refactor
# print(end="Enter a number: ")
# numm = int(input())  # int makes it just a number only
#
# noo = 1
# print("\n Multiplication Table: ")
# for n in range(1, 11):
#     print(str(numm)+ " * " +str(n)+ " = "+str(numm*n))
#
#
# # Third refactor using while Loop
# print("Enter a Number Using a while Loop" )
# NUM = int(input())
# print("\n Multiplication Table:")
# b = 1
# while b < 13:
#     print(str(NUM)+ " * " +str(b)+ " = " +str(NUM*b))
#     b = b+1
#
#
# # having two values
# print("Enter THe Range: ")
# s = int(input())
# e = int(input())
#
# # we conditional statement
# if s==e:
#     numba = s
#     print("----------- Multiplication Table of: "+str(numba)+ "---------")
#     for p in range(1, 11):
#         print(str(numba)+ " * " +str(p)+ " = " +str(numba*1))
# elif s > e:
#     numba = e
#     while numba <= s:
#         print("----------- Multiplication Table of: " + str(numba) + "---------")
#         for p in range(1, 13):
#             print(str(numba) + " * " + str(p) + " = " + str(numba * 1))
#         numba = numba+1
# else:
#     numba = s
#     while numba <= e:
#         print("----------- Multiplication Table of: " + str(numba) + "---------")
#         for p in range(1, 12):
#             print(str(numba) + " * " + str(p)+ " = " + str(numba * 1))
#         numba = numba+1



# using a python to calender but we need to import the calendar
print("Enter Year: ")
yy = input()

print("\n Enter Month Number (1-12): ")
mm = input()

y = int(yy)
m = int(mm)

print("\n", calendar.month(y, m))


# we can also use try-except
# end="" keyword is used in this program to skip inserting an automatic newline using print()
print("Enter Year eg2023: ", end="")

try:
    yyy = int(input())
    print("\n Enter Month Number (1-12): ", end="")
    try:
        mmm = int(input())
        if mmm >= 1 and mmm <= 12:
            print("\n", calendar.month(yyy, mmm))
        else:
            print("\n Invalid Month Number!")
    except ValueError:
        print("\n Invalid Input!")
except ValueError:
    print("\n Invalid Input")


# Displying all Month by using try-except
print("Enter year: ", end="")
try:
    yyyy = int(input())
    print()
    mmmm = 1
    while mmmm <= 12:
        print(calendar.month(yyyy, mmmm))
        mmmm = mmmm+1
except ValueError:
    print("\n Invalid Input!!!")







