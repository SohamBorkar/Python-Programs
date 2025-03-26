# What are lambda functions in Python:
# In Python, an anonymous function is a function that is defined 
# without a name.
# While normal functions are defined using the def keyword in Python,
#  anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions.


# Use of Lambda Function in python:
# We use lambda functions when we require a nameless function for
#  a short period of time.
# In Python, we generally use it as an argument to a higher-order 
# function (a function that takes in other functions as arguments). 
# Lambda functions are used along with built-in functions like filter(),
#  map() etc.

double=lambda x:x*x
print(double(2))

sum=lambda x,y:x*y
print(sum(2,3))

print()

# The filter() function in Python takes in a function and a list 
# as arguments.
# The function is called with all the items in the list and a new
#  list is returned which contains items for which the function 
#  evaluates to True.

# Program to filter out only the even items from a list:

list_old=[1,2,3,4,5,6,7,8,9,0]
newlist=list(filter(lambda x:(x%2==0),list_old))
print(newlist)

# Example use with map():
# The map() function in Python takes in a function and a list.
# The function is called with all the items in the list and a new
#  list is returned which contains items returned by that function
#   for each item.

# Program to double each item in a list using map():

l=[1,2,3,4,5,6,7,8,9,0]
listt=list(map(lambda x:x*2,l))
print(listt)



