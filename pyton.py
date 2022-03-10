#Single line comment = #, multi line comment """ lines""" or ''' lines '''

print("python program successful")

print("Hello,","Soham","Borkar",sep="_")
print("Welcome,",end=" ")
print("Soham")

print()

#another way to print statements:
#import sys
#sys.stdout.write("print statment here")

##predefine variables:
##    __file__ : it will give the name of the current python file.
##    __name__ : when the python module start running directly then the name of python  module is set to __main__.
##    This name is stored in the predefine variable __name__.

print("File location and name is :")
print(__file__)

print()

print("Name of module is set to main as default bcz it doesn't have any main method decleared")
print(__name__)
print()
print()

## If you want to set specific function as main:
def hello():
    print("Hello function here")

if __name__=="__main__":
    hello()
print()
print()

## Keyword number is not fixed in python bcz it adds or minuses as new version comes.
## To see keywords available in installed version of python:
import keyword
print(keyword.kwlist)

print()
print()

## To check if word you want is keyword or not:
print(keyword.iskeyword("True"))

print()
print()

#A reference (i.e. variable) is a name that refers to a point to an object.
#Every item of data in python program is an object of a specific type or class.
#Every object possess a unique ID.
#Decleration of variables/references is not required in python.
#We don't need to specify data type of variables.
#The data type of variable will be decided automatically as per value stored in it.
#The data type of variable will be changed if the value in the variable is changed.
#Keywords cannot be used as variable names.
#Blank spaces are not allowed in variable name.

#To know the type of variable :
x=10
print(type(x))

#To know the ID of variable :
x=10
print(id(x))