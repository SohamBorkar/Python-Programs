#Syntax 1:
# import array as arr
# import imp
# a=arr.array("i",[10,20,30,40,50])
# for x in a:
#     print(x, end=" ")

#Syntax 2:
# from array import *
# a=array("i",[10,20,30,40,50])
# for a in a:
#     print(a, end=" ")

#Syntax 3:
#import array
#a=array.array("i",[10,20,30,40,50])
# for a in a:
#     print(a,end=" ")

# import array as arr
# a=arr.array("i",[10,20,30,40])
# for i in range(0,len(a)): 
#             # or 
# #for i in range(0,a.__len__()):
#     print(a[i],end=" ")



#Array Properties:
#1.: Array typecode and itemsize:
# from array import *
# a=array("d",[10.10,20.20,30.30,40.40])
# print("Typecode is : ",a.typecode)
# print("itemsize is:",a.itemsize, "bytes")








#ArrayFunctions:

#append:

#from array import*
#arr = array("i",[10,20,30,40,30])
# arr.append(50)
# arr.append(10)
# print(arr)

#bufferinfo():
# return a tuple representing the address in which array
#is stored and number of array in that array.
#from array import*
#arr = array("i",[10,20,30,40,30])
# t=arr.buffer_info()
# print(t)
# print(id(arr))

#count(): 
# counts how much times element is present in array.
#it will not work for float array, but will work for double.
# c=arr.count(30)
# print(c)

#extend()
#will add element in the given arr_obj list at the end of current array.
#but the data type of elements in the list or tuple or array must be 
#same as the current array object.
# from array import *
# arr=array("i",[10,20,30])
# l=[40,50]                   #list
# t=(60,70)                   #tuble
# a=array("i",[800,90,100])   #array

# arr.extend(l)
# arr.extend(t)
# arr.extend(a)
# print(arr)


#fromlist():
#it will add the elements from the given list_oject at the end of the 
#current array
#it will accept only list argument.
#data type in the elements in the list and array must be same.
# from array import *
# arr=array("i",[10,20,30])
# l=[40,50]
# arr.fromlist(l)
# print(arr)


#tolist()
#will return all the elements from the array in the list.
# from array import *
# arr=array("i",[10,20,30])
# l=arr.tolist()
# print(type(l))
# print(l)
# print(arr)


#del stmt: to delete elements from arr, list, dicto, user difined obj
#its not able to delete uneditable types like tuple, string and set.
#actually del stmt unbinds references.
#the automatically cleanup of objects to which there are no references
#is known as garbage collection.
#the automatic garbage collection cleans up the unreachable objects.
from array import *
arr=array("i",[10,20,30])
del arr[1]
print(arr)