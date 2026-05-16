class candle:
    def __init__(self,color,height):
        self.color=color
        self.height=height

    def light(self):
        print(f"The {self.color} with a height of {self.height} is lit")


candle1= candle("blue",10)
candle1.light()