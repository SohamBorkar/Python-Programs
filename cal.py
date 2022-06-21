# class cal():
#     def __init__(self, a,b):
#         self.a=a
#         self.b=b
#     def add(self)
#         return self.a +self.b
#     def sub(self):
#         return self.a -self.b
#     def mul (self):
#         return self.a *self.b
#     def div(self):
#         return self.a/self.b

# obj = cal(a,b)








#Practical 22
# Classes and Objects: Write a Program to: Create a Class which Performs Basic Calculator Operations

class Calculator:

    def addition(self):
        print("Additition is ",a + b)

    def subtraction(self):
        print("Substraction is " , a - b)

    def multiplication(self):
        print("Multiplication is ", a * b)

    def division(self):
        print("Division is " ,a / b)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Calculator()

choice = 1
while choice != 0:
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        print(obj.addition())
    elif choice == 2:
        print(obj.subtraction())
    elif choice == 3:
        print(obj.multiplication())
    elif choice == 4:
        print(obj.division())
    else:
        print("Invalid choice")