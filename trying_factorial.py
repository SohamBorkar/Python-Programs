from cmath import pi


def factorial(x):
    if (x==0 or x==1):
        print("Factorial of is 1")
    else:
    #    for i in range(1,x):
    #         y=x*x-1
        # y=x
        for i in range(x,0,-1):         # 5 4 3 2 1
            y=x*(i-1)   # 5*4=20
            y=y*(i-1)    
            print(y)



            # for j in range(i-1,1,-1):
            #     y=y*(x-i)

            
    print(x)


factorial(5)

# 5=120
# 5*4*3*2*1