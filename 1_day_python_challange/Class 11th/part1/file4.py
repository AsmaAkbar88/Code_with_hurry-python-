class Employee():
    a= 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

a = Employee()
print(a.a)   #Output: 1

pro = Programmer()
print(pro.a , pro.b)     #Output: 1 2


man = Manager()
print(man.a , man.b , man.c)   #Output:  1 2 3