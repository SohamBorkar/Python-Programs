# l=[[10,20,30],[40,50,60],[70,80,90]]

# for x in l:
#     print(x)

l=[[10,20,30],[40,50,60],[70,80,90]]

for x in l:
    for y in x:
        print(y, end="  ")
    print()