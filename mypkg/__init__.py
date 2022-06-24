# From init.py we want to we want to call sum function located in calc module
# (calc.py) and return sum using argv.


import calc
# sum('1'.join(''),'2'.join(''))
l=list()
a=int(input("enter how many numbers you want to add: "))
print(a)

for i in range(0,a):
    m=int(input("Enter element: "))
    l.append(m)

print(l)

sum('')