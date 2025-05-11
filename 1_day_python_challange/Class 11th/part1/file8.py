class Number():
    def __init__(self , num):
        self.num = num
    


    def __add__(self , b):
        return self.num  + b.num
    

    def __sub__(self , b):
        return self.num  + b.num
    
    def __mul__(self , b):
        return self.num  - b.num
    
    def __add__(self , b):
        return self.num  * b.num
    
    def __truediv__(self, b):
        return self.num / b.num
    
    

a = Number(4)
b = Number(6)
print(a + b)   #Output:  10
print(a - b)   #Output:  -2
print(a * b)   #Output:  24
print(a / b)   #Output:  0.666



# def __floordiv__(self, b):
#         return self.num ** b.num
    
# print(a ** b)   #Output:  0.666 ye khod sy dkeh lina
