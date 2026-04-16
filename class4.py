class Dog:
    species = "German Sherpherd"

    def __init__(self,name):
        self.name = name

        def bark(self):
            print(f"{self.name} says woof woof")

dog1 = Dog("Rex")
print(dog1.name)
print(dog1.species)

dog2 = Dog("Max")
print(dog2.name)
print(dog2.species)
