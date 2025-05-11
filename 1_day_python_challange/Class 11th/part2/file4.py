class Complex:
    def __init__(self , r , i):
        self.r = r
        self.i = i

    def __add__(self , c2):
        return Complex (self.r + c2.r , self.i + c2.i)
    
    # def __mul__(self , c2):
    #     real_part = self.r * c2.r - self.i * c2.i
    #     img_part = self.r * c2.r + self.i * c2.i
    #     return Complex (real_part , img_part)
    

    def __str__(self):
        return f"{self.r} + {self.i}i"

a = Complex( 1 ,3)

b = Complex(3 , 4)
print(a + b)  #output: (4 + 7i)
# print(a * b)  #output: -9 + 15i