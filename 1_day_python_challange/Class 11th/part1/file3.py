class Employee:
    company = "IBA"
    name = "Asma"
    def show(self):
        print(f"The name is {self.name} and my company is {self.company}")

class Coder():
    language = "Python"
    def print_language(self):
        print(f" Out of all the languages here is your language: {self.language}")

class Programmer(Employee , Coder):
    company = "IBA INFO" 
   
    def showLanguage(self):
        print(f"The company name is {self.company}  and he is a good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company )  #Output:    IBA
print(b.company)   #Output:    IBA INFO


b.show()                # The name is Asma and my company is IBA INFO
b.print_language()      #  Out of all the languages here is your language: Python
b.showLanguage()        # The company name is IBA INFO  and he is a good with Python language

Programmer.print_language(b)     #Output:       Out of all the languages here is your language: Python


