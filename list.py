#List is a collection of elements of different datatypes.
# The list can contain array, tuple, list, string, dictionary and a value 
# like int, float as its member.
# the list can contain duplicate values.
# List can contain duplicate values and elements of different types.
# the list is mutable, iterable and sequence.
# It also supports forward and reverse indexes.
# We can delete elements by using del()

#copying tuple to list:
# t=(10,20,30)
# l=list(t) # here tuple is copied into list l.
# print(l)

#aliasing concept does not work in lists.
#you can change value of elements in list.
#you can add and delete value of elements in list.

# l=[10,20,30,50,60]
# l[0]=20
# del(l[2])
# l.append(40)
# print(l)

#using for in loop in list:
# for x in l:
#     print(x, end=" ")
# #or
# for i in range(0, len(l)):
#     print(l[i],end=" ")


# from typing import Iterable
from array import *
l=[10,1.1,"Soham",[10,20,30],(40,50),array("d",[1.1,2.2,3.3]), {60,70,80},{"a":65,"4":66}];
# print(l)
# print()
# print(l[4][0]) # here we want to print element 40 from the tuple.
# print()   
# for x in l:
#     print(x)

#isinstance():it will return true if the given object belongs to the 
#given data_type otherwise it will return false.

from collections.abc import *
# if isinstance(l[2],Iterable):
#     print('It is an iterable')
# else:
#     print("It is not an iterable")

#Array, dictionary, set, tuple, string, list are part of iterable class
#which belongs collections.abc (abstract base class) package. So you will
# have to impot it as from collection.abc import *

#printing only iterables and elements available from them.
for x in l:
    if isinstance(x, Iterable):
        for y in x:
            print(y,end=" ")
        print()
    else:
        print("It is not Iterable, bcz it may be int or float which is: ",x)  
