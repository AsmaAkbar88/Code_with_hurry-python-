class Employee():
    def __init__(self):
        print("Constructor of Employee")
    a= 1

class Programmer(Employee):
    
    def __init__(self):
        print("Constructor of Progrmaer")
    
    b = 2

class Manager(Programmer):
    
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# a = Employee()
# print(a.a)   #Output: Constructor of Employee  1

# pro = Programmer() 
# print(pro.a , pro.b)     #Output:   Constructor of Manager 1 2


man = Manager()
print(man.a , man.b , man.c)   #Output:   Constructor of Manager  1 2 3