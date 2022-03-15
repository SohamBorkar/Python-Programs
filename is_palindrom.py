n = int(input("Enter a number: "))
m = n 
rev = 0

while n>0:
    x=n%10  #it will find the last digit
    rev=(rev*10)+x
    n=n//10
#end of loop.

if rev==m:
    print("Given number is palindron.")
else:
    print("Given number is not palindron.")
#end of loop