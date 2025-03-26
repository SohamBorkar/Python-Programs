a=9876543210
rev=0
b=0
while a!=0:
    b=a%10
    rev=rev*10+b
    a//=10
    print(rev, end=" ")