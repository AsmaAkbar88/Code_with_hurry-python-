class Employee():
    name = "iqra"    
    language = "PY"
    salary = 120000

    def __init__(self , name , salary , language):
         self.name = name
         self.salary = salary
         self.language = language



    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")
    

result  = Employee("Asma" , 1234500 , "python")     
print(result.name , result.salary , result.language)  #Output:  Asma 1234500 python
print(result.language , result.name , result.salary)  #Output:  python Asma 1234500





# result.getinfo()              #Output:  The language is PY. The salary is 120000
# result.greet()                #Output:    Good Morning
# print(result.language , result.salary , result.name) #Output:    PY 120000 iqra


# Employee.getinfo(result)   #Output:    The language is PY. The salary is 120000