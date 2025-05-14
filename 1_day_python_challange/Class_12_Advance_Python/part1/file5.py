def myfun():
    print("Hello world")

myfun()   #Output:   Hello world
print(__name__)   #Output:   __main__


# _____________________________________


def myfun():
    print("Hello world")

myfun()   #Output:   Hello world


if __name__ == "__main__":
    print("We are directly running this code. ")   #Ouput:   We are directly running this code.
    myfun()                     #Outut:       Hello world
    print(__name__)             #Output:      __main__


# _________________________________________________
