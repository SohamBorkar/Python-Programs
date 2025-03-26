# f=open("soham.txt",'r')
# content=f.read().split(" ")
# print(len(content))
# print(content)






#Practical 20
#File Input/output: Write a program to :
#To open a file in read mode and write its contents to another file but replace every occurrence of character ‘h’ by ‘a’.
# To open a file in read mode and print the number of occurrences of a character ‘a’.
vvvv
# open both files
# # with open('19CM059_PR20.txt','r') as firstfile, open('19CM059_PR20_B.txt','a') as secondfile:
# print("Enter the name of the file to read:", end="")
# file1 = input()
# handle1 = open(file1, "r")
# content = handle1.read()
# handle1.close()
# file2 = str(input("Enter the name of the file to write:"))
# handle2 = open(file2, "w")
# file2 = str(content)
# c = input("ENTER CHARACTER YOU WANT TO REPLACE:")
# r = input("ENTER CHARACTER YOU WANT TO REPLACE WITH:")
# handle2.write(content.replace(c, r))
# handle2.close()


fr=open("soham.txt",'r')
fw=open("soham.txt",'a')

for i in fr:
    fw.write(i.replace('H','N'  ))
#f.write("\n\n")
#f.write("Happy Best of luck")
# replace=f.read()
# replace
# replace.write(content.replace(H,N))
fr.close()
fw.close()