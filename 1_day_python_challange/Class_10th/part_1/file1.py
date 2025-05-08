class Employee():
    name = "iqra"      #This is class attribute
    language = "PY"
    salary = 120000

result  = Employee()
result.name = "Asma"   #This is instance attribute
print(result.language , result.salary , result.name)   #output:   PY 120000 Asma