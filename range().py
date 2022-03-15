# #range():
# print("range() example:")
# for i in range(10,1,-2): #here 2 is the increment value.
#     print(i)

# print("range() example2:")
# for j in range(1,5):
#     for i in range(65,70):
#         print(chr(i),end="") # wanting to print char by giving ascii values.
#     print()

# print("range() pattern of numbers:")

# for j in range(2,6):
#     for i in range(1,j):
#         print(i,end="")
#     print()

# print("range() pattern of charactors:")
# for j in range(66,70):
#     for i in range(65,j):
#         print(chr(i),end="")
#     print()

# print("range() pattern of numbers:")
# for j in range(6,1,-1):
#     for i in range(1,j):
#         print(i,end="")
#     print()

# print("range() pattern of charactors:")
# for j in range(70,65,-1):
#     for i in range(65,j):
#         print(chr(i),end="")
#     print()

#Factorail using range()
n=int(input("Enter a number: "))
f=1
for i in range(1,n+1):
    f=f*i
print("Factorial of %d = %d"%(n,f))