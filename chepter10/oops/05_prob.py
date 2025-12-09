# wa class Train which have a method to book a ticket , get status(no of seats) and get fare information of train running under indian railway

import random


class Train:
    def __init__(self, trainNo):     # this is used to initialize the object
        self.trainNo = trainNo
    
    def bookTicket(self, trainNo, fro, to):
        print(f"ticket book for trainNo : {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"trainNo {self.trainNo} is running on time")
    def getFareInfo(self, trainNo,fro, to):
        print(f"Ticket fare in trainNo {self.trainNo} from {fro} to {to} is {random.randint(220,1000)}")

t = Train(234)
t.bookTicket(2345, "Lucknow", "Delhi")
t.getStatus()
t.getFareInfo(2345, "Lucknow", "Delhi")
