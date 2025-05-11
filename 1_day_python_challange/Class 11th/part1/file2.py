class Employee:
    company = "IBA"
    def show(self):
        print(f"The name is {self.name} and the  salary is {self.salry}")

class Programmer(Employee):
    company = "IBA INFO"

    def showLanguage(self):
        print(f"The name is {self.name}  and he is a good with {self.language} language")




a = Employee()
b =  Programmer()
print(a.company , b.company)   #Output:    IBA IBA INFO

# class Programmer:
#     company = "IBA INFO"
#     def show(self):
#         print(f"The name is {self.name} and the  salary is {self.salry}")

#     def showLanguage(self):
#         print(f"The name is {self.name}  and he is a good with {self.language} language")
