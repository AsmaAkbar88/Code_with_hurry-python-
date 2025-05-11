class Employee:
    company = "IBA"
    def show(self):
        print(f"The name is {self.name} and the  salary is {self.salry}")

class Programmer:
    company = "IBA INFO"
    def show(self):
        print(f"The name is {self.name} and the  salary is {self.salry}")

    def showLanguage(self):
        print(f"The name is {self.name}  and he is a good with {self.language} language")

a = Employee()
b =  Programmer()
print(a.company , b.company)   #Output:    IBA IBA INFO

a.name = "Mona"
a.salry = 9000
a.show()   #output:   The name is Mona and the  salary is 9000