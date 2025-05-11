# class Employee:
#     a = 1

#     def show(self):
#         print(f"The class attibute of a is {self.a}")


# cll = Employee()
# cll.a = 45

# cll.show()   #Output:   The class attibute of a is 45

# _______________________________________________________________________

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attibute of a is {cls.a}")


cll = Employee()
cll.a = 45
cll.show()   #Output: The class attibute of a is 1