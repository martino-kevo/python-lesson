class InsufficientFundError(Exception):
    pass


class BankAccount:

    def __init__(self, initial_amount, account_name):

        self.balance = initial_amount
        self.name = account_name

        print(f"\nAccount '{self.name}' created. \nBalance : ${
              self.balance:.2f}")

    def get_balance(self):
        print(f"\n--- {self.name} --- \nBalance = ${self.balance:.2f}")

    def deposit(self, amount):

        self.balance += amount

        print(f"\nCredit alert! \n${
              amount:.2f} was deposited into your account.")

        self.get_balance()

    def check_withdraw_and_transfer(self, amount):

        if self.balance >= amount:
            return
        else:
            raise InsufficientFundError(
                f"\nInsufficient Fund! {self.name} 🤐 \nBalance in account = ${
                    self.balance:.2f} \nAmount trying to withdraw / transfer = ${amount:.2f}"
            )

    def withdraw(self, amount):

        try:
            self.check_withdraw_and_transfer(amount)
            self.balance -= amount
            print(f"\nDebit alert! \n${
                  amount:.2f} was withdrawn from your account.")
            self.get_balance()
        except InsufficientFundError as error_message:
            print(error_message)

    def transfer(self, amount, account):

        try:
            print('\n************\n\nBegining Transfer... 🚀')
            self.check_withdraw_and_transfer(amount)
            self.withdraw(amount)
            # account.deposit(amount)
            account.balance += amount
            print(f"\nTransfer successful! ✅ \nYou've transfered ${
                  amount:.2f} to {account.name}\n\n\n************")
        except InsufficientFundError as error_message:
            print(error_message)


class InterestRewardsAcct(BankAccount):

    def __init__(self, initial_amount, account_name):

        self.balance = initial_amount
        self.name = account_name

        print(f"\nAccount '{self.name}' created -- Interest Rewards Account. \nBalance : ${
              self.balance:.2f}")

    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print(f"\nDeposit complete! ${
              (amount * 5) / 100:.2f} added to your account balance")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):

    def __init__(self, initial_amount, account_name):

        self.balance = initial_amount
        self.name = account_name
        self.fee = 5

        print(f"\nAccount '{self.name}' created -- Savings Account. \nBalance : ${
              self.balance:.2f}")

    def withdraw(self, amount):

        try:
            self.check_withdraw_and_transfer(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f"\nDebit alert! \n${
                  amount:.2f} was withdrawn from your account.")
            self.get_balance()
        except InsufficientFundError as error_message:
            print(error_message)
