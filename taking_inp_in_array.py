# #Reading Array: is done by append()

# import array as arr

# a=arr.array("i",[])

# for i in range(0,5):
#     a.append(int(input("Enter number to add in array :")))

# print("Array is as follows: ")
# for x in a :
#     print(x, end=" ")

#Taking 5 nos and giving addition of them:
import array as arr

a=arr.array("i",[])
for i in range(0,5):
    a.append(int(input("Enter number to add: ")))

s=0 # to store value of a 
for x in a:
    s=s+x
print("Sum is: ",s)