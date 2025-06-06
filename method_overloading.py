def product(a, b):
	p = a * b
	print(p)

def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error	
# product(4, 5)

# This line will call the second product method,
# beacuse, we may overload the methods but can only
#  use the latest defined method.
 
product(4, 5, 5)







# So efficient way is to use:


# By Using Multiple Dispatch Decorator 
# Multiple Dispatch Decorator Can be installed by: 
# pip3 install multipledispatch


# from multipledispatch import dispatch

# #passing one parameter
# @dispatch(int,int)
# def product(first,second):
# 	result = first*second
# 	print(result);

# #passing two parameters
# @dispatch(int,int,int)
# def product(first,second,third):
# 	result = first * second * third
# 	print(result);

# #you can also pass data type of any value as per requirement
# @dispatch(float,float,float)
# def product(first,second,third):
# 	result = first * second * third
# 	print(result);


# #calling product method with 2 arguments
# product(2,3,2) #this will give output of 12
# product(2.2,3.4,2.3) # this will give output of 17.985999999999997

