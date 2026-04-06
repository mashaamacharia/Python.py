class BirthdayBoy:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def vickie(self):
        print(f"Happy birthday {self.name}! You are turning {self.age}!")

class Wished:
    def __init__(self,name):
        self.name=name
    
    def siz(self):
        print(f"Happy Birthday Big bro wishes from {self.name}")

person=BirthdayBoy("Mashaa","24")
person.vickie()
person1=Wished("siz")
person1.siz()


