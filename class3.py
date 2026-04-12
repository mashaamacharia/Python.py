class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof woof")
        
dog1 = Dog("Buddy")
print(dog1.name) 