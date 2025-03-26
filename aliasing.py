# a li a sing = aliasing means multiple variables pointing to the same ID or data or memory address.

a=5
b=a

#also if we write 
# a=5 
# b=5 
#then also output will be the same, means now also a and b will point to same data or ID or memory area. 

print ("ID of a is: ", id(a))
print ("ID of b is: ", id(b))

print()

if a is b:
    print("ID of a and b is same.")
else:
    print("ID of a and b is not same.")

    # Aliasing concept is not same for immutable or mutable objects.

    