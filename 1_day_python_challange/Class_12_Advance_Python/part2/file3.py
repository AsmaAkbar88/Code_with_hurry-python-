try:
    a = int(input("Entr first number:    "))
    b = int(input("Enter Second number:    "))
    print(a/b)
except ZeroDivisionError  as v :
    print("Infinite")
