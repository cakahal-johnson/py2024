"""
PYTHON COLLECTIONS (ARRAYS)
There are Four collections data types in the python programming language:
---LIST: IS a collection which is ordered and changeable, Allows duplicate members.
--TUPLE: Is a collection which is ordered and Unchangeable, Allows duplicate members.
---SET: This is a collection which is unordered and un-indexed. NO duplicate member.
---DICT OR DICTIONARY: is a collection which is unordered and changeable. No duplicate member.

"""
MyLIst = ["python", "Venza", 80, True, False, "lexus", "kekee", "awesome"]
print(MyLIst)
print(len(MyLIst))
print(type(MyLIst))

# here we get the index
print(MyLIst[2])
print(MyLIst[-2])

# getting the Range
print(MyLIst[2:5])
print(MyLIst[:4])
print(MyLIst[4:])

# checking if item exists: use the keyword: in
if "lexus" in MyLIst:
    print("Yes, we have LEXUS in our database ")


"""
NB: --List item indexed, first item has index [0], while second item will be index [1] ...
    --When ordered, it means that the items have a defined order, the order will not change, but the new item will be
        placed at end
        
"""
# this is a constructor to make a List
# ThisList = tist(("Benz", "Venza", "lexus", "kekee", "Benz"))

# To change the value of a specific item, we refer to the index number
MyList = ["Benz", "Venza", 80, True, False, "lexus", "kekee", "Benz"]
MyList[1] = "Toyota"
print(MyList)

# Changing with range values
MyList[5:7] = ["dog", "ball"]
print(MyList)

# Insert() Items it adds item without removing any item...
MyLisT = ["Benz", "Venza", 80, True, False, "lexus", "kekee", "Benz"]
MyLisT.insert(6, "keke")
print(MyLisT)

# Append Items: to add an item to end of the list, we use append() method:
MyLisT.append("awesome")
print(MyLisT)

# Extend() List: To append elements from another to the current list, use the extend() method.
MyLisT.extend(MyList)
print(MyLisT)

# Adding any Iterable: The extend() method dose not have to append list, you can add any Iterable Object (Tuples, sets)

# Remove specific item: The remove() method removes items
MyLisT.remove("kekee")
print(MyLisT)

# Pop() This removes the specified index.
MyLisT.pop(6)
print(MyLisT)

MyLisT.pop()
print(MyLisT)

# we use the Key Word del also to remove a specific index
del MyLisT[0]
print(MyLisT)

# Clear the List: The clear() method empties the list, but the list still remains...
MyLisT.clear()
print(MyLisT)

# i want this MyLisT empty list to have the same content with MyList
MyLisT.extend(MyList)
print(MyLisT)


# Python - LOOP LIST
# Lets Loop Through a List: to through we the Keyword "for" Loop
# This will print all items in the list, one by one:
for x in MyLisT:
    print(x)

# Python Loops can also Loop through the index Number
# by using range() and len() functions to create a suitable iterable.

for a in range(len(MyLisT)):
    print(MyLisT[a])


# Using a While Loop
# This loop through the list item by using a while loop. and len() function to determine the of the list
i = 0
while i < len(MyLIst):
    print(MyLIst[i])
    i = i + 1

# List Comprehensive: offers the shortest syntax for looping through list
[print(b) for b in MyLIst]

# list comprehensive next topic:
# list comprehensive offers a shorter syntax when you want to create a new list based on the values of an existing list

names = ["Chisom", "chidera", "Mark", "Apple", "app", "Johnson"]
newName = []

for z in names:
    if "a" in z:
        newName.append(z)

print(newName)


name = ["Chisom", "Z", "az", "aa", "chidera", "Mark", "Apple", "app", "Johnson"]
newNames = [u for u in name if "n" in u]
print(newNames)


# The Syntax
# newList = [expression for item in iterable if condition == True]

# checking for condition
nameCheck = [y for y in name if y != "chidera"]
# NOt equal is used to collect data that is in list if not it will print the whole array

print(nameCheck)

# The Iterable can be any iterable object, like a list, Tuple set and others

# you can also use the range() function to create an iterable
counting = [p for p in range(10)]
print(counting)

count = [h for h in range(10) if h < 8]
print(count)

# Expression: is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends
# up like a list item in the new list.

nameUpper = [b.upper() for b in name]
print(nameUpper)

nameHacked = ["Opps! you're hacked" for b in name]
print(nameHacked)

nameTraget = [s if s != "chidera" else "Opps! you're hacked" for s in name]
print(nameTraget)


# SORTING: List object have sort() method that will sort the lis alphanumerically, ascending, by default:
name.sort()
print(name)

Count = [2564, 45621, 100, 2, 50, 99]
Count.sort()
print(Count)

name.sort(reverse=True)
print(name)
Count.sort(reverse=True)
print(Count)

# Customizing Sort Function
# to customize your function you ues the keyword argument key = function which returns the lowest number first

def myOwnFunc(g):
    return abs(g - 50)

inNumber = [251, 325, 0, 44, 50, 28]

inNumber.sort(key = myOwnFunc)
print(inNumber)

name.sort(key = str.lower)
print(name)

Count.reverse()
print(Count)


# Coping In Lists
"""
NB: you cannot copy a list simply by typing list2 = list1, b'cos list2 will only be a reference to list and changes
made in list1 will automatically also be made in list2

so we use the inbuilt list method called copy()
"""

nameNow = name.copy()
print(nameNow)

# Join since there are several ways to join, or concatenate, two or more xlist in python
# am the easiest way by using the + operator.

newList = inNumber + name
print(newList)

for j in name:
    Count.append(j)
print(Count)


Count.extend(name)
print(Count)


"""
List Method you can use to write a function
append() adds an element at the end of the list
clear()  removes all the elements from the list
copy() returns a copied list
count() returns the number of element with the specified value
extend() add the elements of a list(or any iterable), to the end of the current list
index() returns the index of the first elements with the specified values
insert() adds an element at the specified position
pop() removes the item with the specified position
remove() removes the item with the specified value
reverse() reverses the order of the list
sort() sorts the list 

"""