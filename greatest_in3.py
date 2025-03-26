a=float(input("Enter 1st No: "))
b=float(input("Enter 2nd No: "))
c=float(input("Enter 3rd No: "))

if a>b and a>c:
    print(a,"No. is greatest.")
elif b > c:
    print(b,"No. is greatest.")
elif c > b:
    print(c,"No. is greatest.")
else:
    print("All numbers are same.")