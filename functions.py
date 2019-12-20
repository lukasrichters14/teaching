from math import sqrt
# Functions are incredibly useful for any project more than a few lines of code
# (so almost everything). They are essentially pieces of code that you can run
# anywhere in your program to make it more readable and less tedious to write.
# A good rule of thumb is that if you find yourself copying and pasting a chunk
# of code multiple times in your project, it should be made into a function.

def calculate_hypotenuse(a, b):
    ''' Uses the Pythagorean theorem (a^2 + b^2 = c^2) to caluculate the 
    hypotenuse of a triangle. '''
    
    return sqrt(a**2 + b**2)

print("Hypotenuse calculation")
print("a = 3, b = 4, c =", calculate_hypotenuse(3, 4))

#   Above is what is known as a function definition. Let's start with the first
# line. The def keyword tells Python that we are about to define a function. It
# is best practice to define all of your functions outside of the main program,
# i.e. don't define a function inside of another function. I always put them at
# the beginning of my programs, above the main() function. 
#   To the right of the def, is the function name. For function names, the same
# rules for variable naming applies.
#   Inside the parentheses, are the function's parameters. Functions are unable
# to use variables that are not declared inside of its body. So, in order to 
# use other variables, we have to give the function parameters so that the
# values can be used inside the function.
#   The text inside of the three ' characters is called a docstring, it is
# used to explain the overall goal of the function, kind of like a special
# comment.
#   Lastly, the return keyword tells Python what value to give the program that
# called the function. In our case, a user would call our function to
# calculate the hypotenuse of a triangle. Our function should perform the
# necessary calculation and then provide the answer.




# Check out EPLDA.py for a larger program that shows how functions can be used
# to make our lives easier.

