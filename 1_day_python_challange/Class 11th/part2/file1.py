class Two_D_vector():
    def __init__(self , i , j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f" This is a vector i:    {self.i}  j:   {self.j}")
        

class Three_D_vector(Two_D_vector):
    def __init__(self , i , j , k):
        super().__init__(i , j)
        self.k = k

     
    def show(self):
        print(f" This is a vector i:    {self.i}  j:   {self.j}   k: {self.k}")
        

a = Two_D_vector( 2 , 4  )
b = Three_D_vector(3 , 7 , 4)

# a.show()  #Output:        This is a vector i:    2  j:   4
# b.show()    #Output:      This is a vector i:    3  j:   7   k: 4

Two_D_vector.show(a)         #Output:        This is a vector i:    2  j:   4
Three_D_vector.show(b)       #Output:      This is a vector i:    3  j:   7   k: 4