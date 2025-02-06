class BankAccount:
    def _init_(self,account_number,account_holder,balance,account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"you just deposited {amount} into your {self.account_number}")
            print(f"your new balance is {self.balance}")
        else:
            print("you can only deposit a positive amount")
    def withdraw(self, amount):
        self.balance -= 150
        if amount > self.balance:
            print("insuficient funds")
            self.balance += 150
        else:
            print("succesful")
            self.balance += 150 - amount
        print(f"your balance is {self.balance}")

    def check_balance(self):
        print(f"your balance is {self.balance}")

    def transfer(self,amount, target_account):
        self.balance -= 150
        if amount > self.balance:
            print("insuficient funds, transfer unsuccessful")
            self.balance += 150
        else:
            self.balance += 150 - amount
            target_account.balance += amount
            print("transfer succesful")
            
a = BankAccount(787878787, "mofe", 60000, "savings")
b = BankAccount(989989898,"Tise", 90000, "current")

#deposits
a.deposit(70)
b.deposit(-23)

#withdrawals
a.withdraw(60000)
b.withdraw(700)

#check balance
a.check_balance()
b.check_balance()

# transfer funds
a.transfer(800,b)