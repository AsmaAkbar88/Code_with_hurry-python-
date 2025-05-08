class Employee():
    name = "iqra"
    language = "PY"
    salary = 120000


    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

result  = Employee()
result.getinfo()         #Ouput:  The language is PY. The salary is 120000
print(result.language , result.salary , result.name)  #OUTPUT: PY 120000 iqra