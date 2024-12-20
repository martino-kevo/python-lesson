from bank_accounts import *

dave = BankAccount(1000, 'Dave')
sarah = BankAccount(2000, 'Sarah')

dave.get_balance()
sarah.get_balance()

sarah.deposit(500)

dave.withdraw(10000)
dave.withdraw(10)

dave.transfer(10000, sarah)
dave.transfer(100, sarah)
sarah.get_balance()
print()

jim = InterestRewardsAcct(1000, 'Jim')

jim.get_balance()

jim.deposit(100)

jim.transfer(100, dave)

dave.get_balance()

blaze = SavingsAcct(1000, 'Blaze')

blaze.get_balance()

blaze.deposit(100)

blaze.transfer(1000, sarah)
blaze.withdraw(100)
blaze.deposit(5)
blaze.withdraw(100)

print()
