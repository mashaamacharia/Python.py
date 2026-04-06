class Dog:
    def __init__(self,name):
        self.name=name
    
    def bark(self):
        print(f"{self.name} says woof woof woof")
    
    class dog1:
        def __init__(self,name):
            self.name=name
        
        def lick(self):
            print(f"{self.name} says elf elf elf")

    dog0=dog1("Tom")
    dog0.lick()
dog1=Dog("Bosko")
dog1.bark()
    