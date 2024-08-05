"""
PYTHON DICTIONARY:
SO THIS IS USED TO STORE DATA VALUES IN KEYS AND VALUE PAIRS
    syntax: we start with curly brackets and have keys: values
    this dict is a collection which is ordered, changeable and does not allow duplicates
"""
print("=====================Python Dict Starts Here ==================")
myAcc = {
    "name": "Savings Account",
    "account_No:": 123456789,
    "balance": 999
}

print(myAcc)

# where we want to pick or printout an item as Array
print(myAcc["balance"])

# checking for the array length with len() method
print(len(myAcc))

# where we check for datatype which returns the class
print(type(myAcc))

# we can also use get() to return the same result
acc = myAcc["account_No:"]
print(acc)
Acc = myAcc.get("name")
print(Acc)

# here we Key() method to return a list of all the keys in the dictionary
acc_details = myAcc.keys()
print(acc_details)

# lets add more details to acc
myAcc["email"] = "example@gmail.com"
print(acc_details)

# let credit the acc
myAcc["credit"] = 4000
myAcc["balance"] = 4999
print(myAcc)

# here we get the values with values()
acc_info = myAcc.values()
print(acc_info)

# lets update from savings to current
myAcc["name"] = "current_Account"
print(acc_info)

# with item() this returns each item in a dict as tuples in a list
acc_group = myAcc.items()
print(acc_group)

# check for deposit in the acc
if "deposit" in myAcc:
    print("yes, 'deposit' is already made in this acc!")
else:
    print("no Deposit yet!")


# where we can update both the keys and values
myAcc.update({
    "name": "cakahal Johnson"
})

print(myAcc)

# removing both we use pop()
myAcc.pop("credit")
print(myAcc)

#  here we use popitem method to remove the last inserted item (from version 3.7, a random item is removed instead)
# myAcc.popitem()

# to delete we can also use del keyword to remove item with specified key name:
# del myAcc['balance']

# NB: del can also delete the dictionary completely
# del myAcc
# if you del the dict and still wants to print myAcc it gives error b'cos myAcc is no longer exists


# where we clear() method to empty the dictionary
# myAcc.clear()
# print(myAcc)
print(myAcc)


print("================== next class LOOPs ===========================")
# Note: when looping, the return value are the keys but some method can return the values as well

myCar = {
    "brand": "Benz",
    "model": "GLK",
    "year": 2023,
    "email": "example@gmail.com",
    "color": ["red", "white", "black"]
}

print("getting the Keys")

for car in myCar:
    print(car)

print("getting the Values")
for cars in myCar:
    print(myCar[cars])

print("we can also use values() method to return")
for Car in myCar.values():
    print(Car, "\n")

print("same as using keys() to return the keys in dict ")
for CAR in myCar.keys():
    print(CAR)

print("here we use item() method to get both keys and values ")
for caR, cAr in myCar.items():
    print(caR, cAr)

print(myCar)

print("dictionaries coping")
myKeke = myCar.copy()
print(myKeke)

print("another way to copy a dict ")
myBus = dict(myKeke)
print('myBus', myBus)
print('myCar', myCar)
print('myKeke', myKeke)


print("======================Nested Dict +++++++++++++++++++========")

# Nested Dict: this is where a dict can contain another dictionaries, it's called Nesting Dictionary
myStudent = {
    "Java": {
        "name": "Johnson",
        "year": 2020
    },
    "Web Dev": {
        "name": "Cakahal",
        "year": 2010
    },
    "Python": {
        "name": "Peter",
        "year": 2023
    }
}

print(myStudent)

for student in myStudent:
    print('Nested keys only : ', student)

for stud, course in myStudent.items():
    print(stud, course)

# another ways of creating this dict that will contain other dict
myCourse = {
    'name': "Python",
    'no_of_student': 200
}

myCourse2 = {
    'name': "Java",
    'no_of_student': 150
}

myCourse3 = {
    'name': "Web Development",
    'no_of_student': 500
}

all_my_Course = {
    'myCourse': myCourse,
    'myCourse2': myCourse2,
    'myCourse3': myCourse
}

print('all my course : ', all_my_Course)

# here to remove all elements from a dict list clear() it only removes the items inside
print('checking the item side myBus variables', myBus)

# to clear using clear()
myBus.clear()
print('checking the item side myBus variables', myBus)

print('checking the item side myCar variables', myCar)

# to delete using del keyword
#del myCar
#print('checking the item side myCar variables', myCar)
#  NameError: name 'myCar' is not defined

try:
    del myCar
    print('checking the item side myCar variables', myCar)
except NameError:
    print('checking NameError: ', "An Error occured!")


# fromkeys() methods returns a dict with the specified keys and the specified value
# syntax: dict.fromkeys(keys, values)

# where: Keys Required, an iterable specifying the keys of the new dict
# where: value Optional. the value for all keys Default value is none

bar = ('key1', 'key2', 'key3')
site = 100
foundation = "work"
building = dict.fromkeys(bar, site)
print('using fromkeys keyword: ', building)

building = dict.fromkeys(bar, foundation)
print('using fromkeys keyword: ', building)

# copy()
# get()
# update()
# item()
# pop()
# popitem()
# values()


# setdefault() method returns the value of the item with the specified key, if the key does not exist, insert the
# key, with the specified value...
"""
SYNTAX: dictionary.setdefault(keyName, value)
where KeyName: is Required, the keyName of the item you want to return the value from
where Value: is Optional, if the key exist, this parameter has no effect, is the key does not exist,
this value becomes the keys's value---then Default value None

"""

myCar = {
    'Brand': "Lexus Black",
    'Model': "RX 750",
    "year": 2023,
    'email': 'example@gmail.com'
}

bye_bye = myCar.setdefault('color', 'white')
print('printing my Setdefault color: ', bye_bye)

print('printing for the items in my dream Car: ', myCar)


byeBye = myCar.setdefault('color')
print('printing my Setdefault color: ', byeBye)





