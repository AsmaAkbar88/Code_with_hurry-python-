class Demo():
    a = 5

result = Demo()   #print the class attribute
print(result.a)       #Output:  5

result.a =  10  #instance attribute is set
print(result.a)       #Output:  10

print(Demo.a)   #Print class attribute   #Output:  5