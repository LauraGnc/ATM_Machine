# script class bank account

class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as fi:
            self.balance = int(fi.read())
            fi.close()

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as f:
            f.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        # transfer CHECKING money to ACCOUNT.
        self.balance -= (amount + self.fee)
        your_account.deposit(amount)


'''
your_account = Account('balance')
your_checking = Checking('checking_balance', 5)

your_checking.transfer(100)
your_checking.commit()
your_account.commit()

print("Checking account: ", your_checking.balance)
print("Main account: ", your_account.balance)

'''