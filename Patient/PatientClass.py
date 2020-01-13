class patients:
    def __init__(self, name, contact, age, days, balance):
        self.name = name
        self.contact = contact
        self.age = age
        self.days = days
        self.balance = balance

    def getName(self):
        return self.name
    def getContact(self):
        return self.contact
    def getAge (self):
        return self.age
    def getDays (self):
        return self.days
    def getBalance (self,):
        return self.balance
    def updateName(self, name):
        self.name = name
    def updateContact(self, contact):
        self.contact = contact
    def updateAge(self, age):
        self.age = age
    def updateDays(self, days):
        self.days = days
    def updateBalance(self, discount):
        self.balance = self.balance - ((discount * 0.01)* self.balance)
