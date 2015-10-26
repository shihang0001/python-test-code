__author__ = 'shihang'

print "Welcome to Python!"



# Bringing It All Together
# Nice work! So far, you've learned about:
#
# Variables, which store values for later use
# Data types, such as numbers and booleans
# Whitespace, which separates statements
# Comments, which make your code easier to read
# Arithmetic operations, including +, -, *, /, **, and %





my_variable = 10
# //set the variable;

a=True
b=False
# set the boolean part of the python

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int =3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

print my_int





# IndentationError: expected an indented block


def spam():
    eggs = 12
    return eggs

print spam()


"""Sipping from your cup 'til it runneth over,
Holy Grail.
"""
# special comment of structure line

addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9
print addition
print subtraction
print multiplication

eggs =10** 2
print eggs

spam =3 % 2
print spam

# using the command to solve the math problem
# here

meal = 44.50
tax = 0.0675
tip = 0.15
meal = meal + meal * tax
total=meal+meal*tip
print("%.2f" % total)
#inictial the total number


# The string below is broken. Fix it using the escape backslash!
'This isn\'t flying, this is falling with style!'




"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "PYTHON"[2]
print fifth_letter



parrot="Norwegian Blue"
len(parrot)
print len(parrot)
parrot.lower()
print parrot.lower()
parrot.upper()
print parrot.upper()
pi=3.14
str(pi)
print str(pi)
#make number to string
#string method

# Print the concatenation of "Spam and eggs" on line 123
print "Spam " + "and " + "eggs"
print "The value of pi is around " + str(3.14)
print


"String Formatting with %, important"


string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'This a silly %s." % (string_1, string_2)


print "I am a {type}".format(type="string")
my_name = "Michael"
print "Hello, my name is {name}".format(name=my_name)
print ""

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s your quest is %s, " \
"and your favorite color is %s."   % (name, quest, color)



'Alpha'
"Bravo"
str(3)
#String methods

len("Charlie")
"Delta".upper()
"Echo".lower()
#Printing a string

print "Foxtrot"
#Advanced printing techniques

g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)