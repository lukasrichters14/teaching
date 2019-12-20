from math import sqrt  # Don't worry about this for now.

# This is a comment. A commment helps people read your code and understand what
# is going on. When the computer tries to run your program, all comments are
# ignored. They are purely for people to read. In Python, a commment is denoted
# by the # character. Generally, comments are placed above, or on the same line
# as, the thing that they are describing.



# A variable is a placeholder for a value, similar to x and y in algebra. To 
# declare (create) a variable, you just type the name (almost anything works) 
# and assign it a value with the = character.
var = 3


# There are a few exceptions when naming variables. They MUST start with a
# letter, no punctuation (other than _ ) or numbers allowed at the beginning. 
# Numbers are allowed in the name, just not at the beginning.


# Here are a few more variables.
some_text = "Hello World!"
x = 4
y = 3.5
z = True


# Now that you understand variables, let's look at types of variables. In the
# five variables above, there are four different types used. Types of
# variables define what operations can be performed on variables of that type
# and how they interact with other variables. The types of variables can be
# seen with the Python type() function as shown below.

print("Types")
print(type(var))  # Integer (int).
print(type(some_text))  # String (str).
print(type(x))  # Integer (int).
print(type(y))  # Float (float).
print(type(z))  # Boolean (bool).
print("\n")

# We use the Python print() function to display information to the console
# (to the user).


# Now, we should talk about the types used here.
# String - a sequence of characters. It can hold anything that you can type on
# a keyboard.
# Integer - a whole number (no decimal point).
# Float - a number with a decimal point.
# Boolean - either the value True or False, nothing else.


# I'll talk about strings and booleans in another module, since they are a little bit more
# complicated. Integers and floats are pretty basic types. They can be used
# with all of the mathematical operators:
#   Addition (+)
#   Subtraction (-)
#   Multiplication (*)
#   Division (/)
#   Power (**)
#   Modulus (%)
# and that's about it.


# Here are some examples.
print("Int and float examples")
a = 7
b = 12
print(a + b)

c = 1.5
print(a + c)
 
# Here's the quadratic formula.
quad_formula_plus = (-1 * b + sqrt(b**2 - 4 * a * c)) / 2 * a
quad_formula_minus = (-1 * b - sqrt(b**2 - 4 * a * c)) / 2 * a
print(quad_formula_plus)
print(quad_formula_minus)
