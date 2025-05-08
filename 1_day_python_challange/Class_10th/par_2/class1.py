class Programmer():
    company = "Microsoft"

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

result = Programmer("Asma Abar " , 132000)
print(result.name , result.salary , result.company)   #Ouput:   Asma Abar  132000 Microsoft
        