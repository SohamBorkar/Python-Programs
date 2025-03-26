x='1'
print(type(x))
y=int(x)
print(y)
print(type(y))
y=float(y)
print(y)
print(type(y))
#y=chr(y)        #to get ascii value of the given integer in charactor format. but here it will throw an error bcz we given float value insted of integer.
print(type(y))

a=int("1111",2)# 1111 is binary, so it will convert to decimal number.
print(a)

b=int("f",16)#it's hexadecimal
print(b)

b=int("17",8)#it's octal
print(b)

b=int("15",10)#it's decimal
print(b)

print()

z=ord('A')# it gives ascii value of charactor and special charactors.
print(z)
print(type(y))

z=ord('0')# it gives ascii value of charactor and special charactors.
print(z)
print(type(y))

z=ord('$')# it gives ascii value of charactor and special charactors.
print(z)
print(type(y))

#bool:
u=[]
print(bool(u)) #False

u=[0]
print(bool(u)) #True

u=0.0
print(bool(u)) #False

u=None
print(bool(u)) #False

u=True
print(bool(u)) #True

u="easy stirng"
print(bool(u)) #True
