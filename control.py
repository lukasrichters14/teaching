# In the variables module, we talked about the boolean type. Booleans are very
# important for controlling the flow of programs. A quick reminder: booleans
# can only be True or False, nothing else.

# The if-else statement.
print("if-else")
if 5 > 3:
    print("5 is greater than 3")

else:
    print("5 is less than 3")

print("\n")
    
# So, obviously 5 is greater than 3. That means that when this program is run,
# it will output "5 is greater than 3" and then exit. But what is actually
# going on? The > operator is taking its two inputs, 5 and 3, and returning the
# value True, since 5 > 3 is true. Then, the if statement reads the value as
# True, which means that it has to execute the code under it.

# If statements look for True values. If it sees a False value, it DOES NOT
# execute the code below it. Instead, the code under the else (if it exists) is
# run.


# The while statement.
print("while")
x = 0
while x < 10:
    x = x + 1
    
print(x)
print("\n")

# The while statement is very handy. The code below it continues to run as long
# as its condition is true. In this case, x starts out as 0 and increases by 1
# each time the while loop is run. This is because x < 10 is true until x = 10.
# At that point, x < 10 is False, and the while loop DOES NOT run.


# Example. This program counts the number of even and odd numbers from 0 to 100,
# not including 100.

i = 0
num_of_evens = 0
num_of_odds = 0

while i < 100:
    if i % 2 == 0:
        num_of_evens += 1
    else:
        num_of_odds += 1
    
    i += 1

print("Number of evens:", num_of_evens)
print("Number of odds:", num_of_odds)


# Let's unpack this. We initialize 3 variables. One holds the current number 
# (i), and the other two hold the number of odds and evens. The while loop runs
# until the number 100, then stops. The mod operator (%) is the remainder of a
# division operation. We know that if 2 divides i evenly (i / 2 = a whole
# number. Same as i % 2 = 0), then i is an even number. In that case, we add 1 
# (+= 1) to the num_of_evens variable. If not, then we add to the num_of_odds
# variable.