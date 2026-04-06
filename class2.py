class Dog:
    def __init__(self,name):
        self.name=name
    
    def bark(self):
        print(f"{self.name} says woof woof woof")
dog1=Dog("Bosko")
dog1.bark()
    