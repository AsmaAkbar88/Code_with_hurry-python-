class Employee():
    salry = 30000
    increment = 30

    def salary_After_Increment(self):
        return (self.salry + self.salry * (self.increment/100))

a = Employee()
print(a.salary_After_Increment())  #Output:   39000


# ______________________________________________________________________________



class Employee():
    salry = 30000
    increment = 30
    
    @property
    def salary_After_Increment(self):
        return (self.salry + self.salry * (self.increment/100))
    

    @salary_After_Increment.setter
    def salary_After_Increment(self , salry):
        self.increment = ((salry/self.salry ) -1 )*100

    

# a = Employee()
# print(a.salary_After_Increment)

# a.salary_After_Increment = 39000.0
# print(a.increment)
