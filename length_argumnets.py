# *argv
def argv(*argv):
    for i in argv:
        print(i)
    print()
    print(argv)
    print()

argv('any', 'values', 'here')


# **kwargs
def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" %(key, value))
    print()
    print(kwargs)

myfun(name="soham", surname="Borkar", age="19")


# To print *argv and **kwargs in same function:
# def myFun(*args,**kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
  
  
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")