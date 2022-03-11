x,y=1,2

print(x,"           ",y)
print(id(x), id(y))

y, x=x, y

print(x,"            ",y)
print(id(x), id(y))