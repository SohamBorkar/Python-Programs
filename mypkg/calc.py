# def sum(*argv):
#     for i in int(argv):
#         i+=i
#     print("Sum is: ",i)

# from ast import arg

# From init.py we want to we want to call sum function below and return sum using argv.
def sum(*argv):
    argv+=argv
    return(argv)