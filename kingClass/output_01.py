# this is a comment single line comment
"""
Multiple line comment

Content here
Anything inside is a comment

#variable

Rules for constructing names for variables:
—Names can only contain letters, underscores
—Variable cannot start with a name
—very very case-sensitive I.e name and Name is not the same

surName is camel case (each word, except the first letter to start with a capital letter )

Sur_name is snake case (each word is separated by an underscore)

MyNameOne is pascal case (each word starts with a capital letter)

Low case, upper case, word and number

"""


# Syntax
#variableName assign(=) value
Name = 'cakahal'  #string
Age = 70 #number

#outputting variables
print(Name)
print(Age)

#Casting variables
#Where a data type is passed as another data type

X = str(70) # X will be “70”
Y = int(70) # Y will be 70
Z = float(70)  # will be 70.0

#checking the variables data type
print(type(X)) # this will return the data type

#Multiple variables
A, B, C = 'Java', 'python', 'php'
print(A) # Return Java
print(B) # return python
print(C) # returns php