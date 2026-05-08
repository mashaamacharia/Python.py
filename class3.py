class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof woof")
class Cat:
    def__init__(self,name):
        self.name=name

cat1=Cat("Whiskers")
print(cat1.name)
dog1 = Dog("Buddy")
print(dog1.name) 