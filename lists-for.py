# Another extremely important data type in Python is the list. A list is an
# ordered collection of elements. It's easier to show you.

a_list = ["Sam", 3, 4.5, "Kevin"]

# This list has 4 elements. Two strings, an integer, and a float. Now, what if
# we want to look at just one element in this list? We'd have to use the
# index operator [].
print("List indices")
print("element 1:", a_list[0])  # Sam
print("element 2:", a_list[1])  # 3
print("element 3:", a_list[2])  # 4.5
print("element 4:", a_list[3])  # Kevin
print("\n")

# If you look closely you'll notice something interesting. Element 1 starts at
# 0 in the list. This is very important to remember.


# Another very useful tool when working with lists is the .append() member
# function. .append(x) places x at the end of the list. To use .append(),
# simply type the variable name of your list, then add .append(x) (where x is
# some variable or value) to the name.

print("Append")
a_list.append("Stacy")
print(a_list)
print("\n")

# As a brief aside, .append() is member function. A member function is one that
# is type-dependent and is an operation defined as part of what makes up that
# type. For example, trying to .append() to an integer will create an error.


# Now that we know a little bit about lists, we can use them to introduce the
# concept of the for loop. A for loop is one that runs an explicit amount of
# times. This can be over a collection (like a list) or for a set number of
# iterations.

print("for loops")
for i in a_list:
    print(i)

print("\n")


# This for loop goes over each element of the list a_list and prints it. To do
# this, in the first loop the value a_list[0] is assigned to the variable i.
# Then, the value of i is printed. It repeats this process for each element in
# the list, assinging the value to i, and printing it.


# Example. Calculates and displays the first 50 Fibonacci numbers.

print("Fibonacci")
fibonacci_list = [0, 1]
index_1 = 0
index_2 = 1

for i in range(50):
    temp = fibonacci_list[index_1] + fibonacci_list[index_2]
    fibonacci_list.append(temp)
    index_1 += 1
    index_2 += 1

print(fibonacci_list)


# Fibonacci numbers are calculated by adding the last two numbers in the
# sequence together to get the next number. To begin the calculation, the first
# two numbers are 0 and 1, which are the first two elements in our list. The 
# range(x) function returns a list with the elements [0,...,x-1]. This allows
# us to calculate the exact number of values we want, in this case 50. Two
# variables index_1 and index_2 are used to keep track of which numbers to add
# together, and are incremented by one with each iteration of the for loop.
# The calculation proceeds by adding the two elements denoted by index_1 and
# index_2 together, and then appending it to the list so it can be used in the
# next iteration.