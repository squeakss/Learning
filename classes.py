# a class is a blueprint for creating objects. an object has properties and methods (functions) associated with it. almost everything in python is an object.

#create a class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f'my name is {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age += 1




#extend class
class customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
        
    def greeting(self):
        return f'my name is {self.name} and i am {self.age} and my balance is {self.balance}'    
        
#initialize user object
b = User('', '', )
#initiate customer object
n = customer('', '', )

n.set_balance(500)
print(n.greeting())

b.has_birthday()
print(b.greeting())
