class Employee():
    name = "iqra"    
    language = "PY"
    salary = 120000


    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")
    

result  = Employee()         
result.getinfo()              #Output:  The language is PY. The salary is 120000
result.greet()                #Output:    Good Morning
print(result.language , result.salary , result.name) #Output:    PY 120000 iqra


Employee.getinfo(result)   #Output:    The language is PY. The salary is 120000