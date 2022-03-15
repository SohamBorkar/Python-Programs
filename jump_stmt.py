# #break stmt:
## if specified condition occured then just go out of loop is the work of break.
# for i in range(1,6):
#     print(i)
#     i+=1
#     if i ==5:
#         break

## continue stmt:
##if specified condition occured then skip the good part (next iteration) is the 
##work of continue statement.
# i=0
# while i<10:
#     i+=1
#     if i%2==0:
#         continue
#     print(i,end="")

## pass stmt:
## will do nothing. it is created when we know we are going to develope the 
## class we mentioning but now we don't have any clue about that so we just 
## created that class.
## We create class and use pass there bcz if we just created class, then it may
## give error to us.
def add(x,y):
    print("Happy")
    pass
    print("Birthday")

add(10,11)