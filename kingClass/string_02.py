# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
# Slicing Negative indexing
#This uses -ive index to start the slice from end of the string
#while in slice to end will be picking from back, but always by leaving out the end index, the range it will got to the end...

#todays topic on String Formats
#string format in concatination
course = "python"
course_title = " py101"
show_course = course + course_title
print(show_course)

#string format in format() method passing in a variable inside a string

Btc_rate = 880
Usdt = 750
us = "USDT"
jp = "BTC"
name = "Ozo"
Name = "cakahal"
Buyer = "i want some BTC at, {} rate"
print(Buyer.format(Btc_rate))
print(Buyer.format(Usdt))

new_buyer = "{} want to buy some {}, at {} rate"
print(new_buyer.format(name, us, Usdt))
print(new_buyer.format(Name, jp, Btc_rate))

old_buyer = "{1} want to buy some {0}, at {2} rate"
#number is always a position index not a dataType
print(old_buyer.format(name, us, Usdt))

#f"" format for string

# String Modifiers
txt = "   hello world!    "
print(txt.upper())
print(len(txt))

#Removing Whitespace in string strip() it remove space at the starts and the end
text = "    Cakahal Johnson "
print('before the strip word', text)
check_len = len(text) #len() is a primitive function while text is non-primitive

print('before the strip(): ', check_len)

# to get the actual lenght of the text string
actual = text.strip() #.strip removes the white space

print('after the strip():', actual)

print('after the strip(): ', len(actual))

# Replace in strings
Text = "Ozo"
print(Text.replace("O", "U"))

# we are done with strings
# String: means word by character using " " or ' '

# List: stores multiple items in a single variable using square brackets []

# Tuple: stores multiple items in a single variable using ()
# the collection is ordered and unchangeable

# Set: stores multiple items in a single variable using {}


# Dictionatry:
