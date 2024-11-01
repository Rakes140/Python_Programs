class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =:", self.get_balance() )

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =:", self.get_balance())
    
    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 986732324545)
acc1.debit(2000)
acc1.credit(50000)
        