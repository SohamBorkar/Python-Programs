# Creating Classes and Objects:

from traceback import print_tb


class parrot:
    #class attribute
    species="bird"
    parous="oviparous"

    #instance attributes
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sing(self, song):
        return "{} sings {}".format(self.name,song)

    def dance(self, dance):
        return "{} dances".format(self.name)

#instianciate/ initialization of the parrot class:
blu=parrot("Blu",4)
blu2=parrot("Blue2",7)

#access the class attributes:
print(blu.species)
print(blu.parous)
print("Blu is a {}".format(blu.__class__.species))
print("Blu is a {}".format(blu.__class__.parous))

print(blu2.__class__.species)
print(blu2.__class__.parous)
print("Blu2 is a {}".format(blu.__class__.species))
print("Blu2 is {}".format(blu2.__class__.parous))

print()

#accessing the instance attributes:
print(blu.age)
print(blu2.age)
print("blu age is {}".format(blu.age))
print("blu2 age is {}".format(blu2.age))

print()

#calling instance methods.
print(blu.sing("Happy Birthday Song"))
print(blu.dance(""))
    