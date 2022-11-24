


class user:
    def __init__(self,name, age , gender):
        self.name = name
        self.age = age 
        self.gender = gender

    def Details(self):
        print("Account details:")
        print(f"name: {self.name}\nage: {self.age}\ngender: {self.gender}")  


class Bank(user):
    def __init__(self, name, age, gender):
        
        super().__init__(name, age, gender)
        self.balance = 0    
        
    def deposit(self,amount):
         self.balance = self.balance + amount
         print(f"Account balance has been updated: ${self.balance}")

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Error| Balance Available:${self.balance}")
        else:
            self.balance = self.balance - self.amount 
            print(f"Account balance has been updated: ${self.balance}")
    def show_balance(self):
        self.Details()
        print(f"Your Balnace is: ${self.balance}")






#one = user("ahmed",21 , "male")
#one.Details()
one1 = Bank("Joo",22 , "male")

one1.deposit(100)
one1.withdraw(200)
one1.show_balance()
