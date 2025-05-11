class Vector():
    def __init__(self , l):
       self.l = l


    def __len__(self):
        return len(self.l)
    

v1 = Vector([1 , 2, 3 , 7, 6 ])
v2 = Vector([4 , 5, 6 , 6])
v3 = Vector([7 , 8 ,9])


print(len(v1))   #OUTPUT:     Vector 5i + 7j + 9k
print(len(v2))   #OUTPUT:     Vector 5i + 7j + 9k
print(len(v3))   #OUTPUT:     Vector 5i + 7j + 9k
