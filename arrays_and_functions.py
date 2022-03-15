import array

arr=array.array("i",[10,20,30,40,50])
#or we can also use:
# s="Soham"
#for x in s:
#   print(s)

print(arr)
print(arr[1])

#if we want to access elements of array one by one.
for x in arr:
    print(x, end=" ")
#end of loop