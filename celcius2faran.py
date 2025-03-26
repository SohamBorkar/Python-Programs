i=input("Enter 1 Celcious or Enter 2 for Ferenheit: ")
i=int(i)

#if i==1 | i==2:
if i==1:
    c=float(input("Enter Celcious: "))
    F=c*9.0/5.0 + 32
    print(c,"Celcius means",'%.4f'%F,"Faranheit")
if i==2:
    f=float(input("Enter Faranheit: "))
    C=(f- 32) * .5556
    print(f,"Faranheit means",'%.4f'%C,"Celcious")
else:
    print("Please enter right input.")



    



