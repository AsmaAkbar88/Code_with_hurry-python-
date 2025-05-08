from random import randint

class Train():
    def __init__(self , trainNo):
        self.trainNo = trainNo


    def book(self , frm , to):
        print(f" Ticket is booked in train no: {self.trainNo} from {frm} to {to}")

    def get_status(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self , frm , to):
        print(f" Ticket fare in train no: {self.trainNo} from {frm} to {to} is {randint(333 , 555)}")


t =Train(134644)
t.book("Karachi " , "Lahore \n")

t.get_status()

t.getFare("Larkana" , "Karachi Cant\n")