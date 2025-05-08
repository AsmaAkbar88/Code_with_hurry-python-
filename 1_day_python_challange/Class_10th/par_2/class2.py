class Calculator():
    def __init__(self , num):
        self.num = num
    

    def square(self):
        print(f"This is a square {self.num * self.num}")
        

    def  cube(self):
        print(f"This is a cube {self.num * self.num * self.num}")
        

    def square_root(self):
        print(f"This is a square {self.num ** 1/2}")
        

result = Calculator(4)
result.square()

result.cube()

result.square_root()