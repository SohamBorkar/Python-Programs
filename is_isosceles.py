a=float(input("Enter 1st Angle: "))
b=float(input("Enter 2nd Angle: "))
c=float(input("Enter 3rd Angle: "))

if (a+b+c == 180) and (a==b or b==c or c==a):
    print("Given triangle is Isosceles Traingle.")

else:
    print("It is not Isosceles Triangle.")
    
# end if