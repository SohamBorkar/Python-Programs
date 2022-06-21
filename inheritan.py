class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printname(self):
        print(self.name + " is " + str(self.age) + " years old.")

class son(person):
    pass

x=son("Rahul",20)
x.printname()