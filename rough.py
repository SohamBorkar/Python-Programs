student_name = 'Rahul'

marks = {'Pawan': 90, 'Rahul': 55, 'Roshan': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
else:
    print('No entry with that name found.')

dict = {'Vegetables' : ['Cabbage', 'Tomato', 'Onion'], 'Fruits' : ['Apple', 'Mango', 'Banana'], 'Flowers' : ['Rose', 'Lotus', 'Lily']}

# print(dict)
# print(dict['Vegetables'] [0])
# print(dict['Fruits'] [1])

for i,j in dict.items():
    print(i,end=" : ")
    print(j[0],j[1],j[2])
    

# for i,j in dict.items():
#     print(j[0],",",end=" ")
#     print(j[2])

# for i in range (0,3):
#     print(dict['Vegetables'][i])

# for i in dict:
#     print(i)
#     for j in dict[i]:
#         print(j)

# print()

# print(dict['Vegetables'])
# print(dict['Fruits'])
# print(dict['Flowers'])

# print()

# print(dict['Vegetables'][0])
# print(dict['Fruits'][1])
# print(dict['Flowers'][2])



