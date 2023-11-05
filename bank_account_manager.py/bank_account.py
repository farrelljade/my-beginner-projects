# define an exception class to deal with insufficient funds. (- balances)
class FundsException(Exception):
    pass

class BankAccount:
    # initialise bank account with account name and balance
    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.balance = balance
        print(f"\nBank account created for: {acc_name}\nAcoount balance: £{balance:.2f}.")
    
    def check_balance(self):
        # Display the current bank balance
        print(f"\nYour current balance is: £{self.balance}")

    def deposit(self, deposit_amount):
        # deposit funds into the account and update the balance
        self.balance = self.balance + deposit_amount
        print(f"\nDepositing £{deposit_amount:.2f}...\nDeposit complete.\nAccout balance: £{self.balance:.2f}.")

    def enough_funds(self, amount):
        if self.balance >= amount:
            return
        else:
            # checking there are enough funds using the exception class
            raise FundsException(f"Insufficient funds.\nAccount balance: £{self.balance:.2f}.")

    def withdraw(self, amount):
        try:
            # checking/withdrawing funds
            self.enough_funds(amount)
            self.balance = self.balance - amount
            print(f"\nWithdrawing £{amount:.2f}...\nWithdrawal complete.\nAccount balance: £{self.balance:.2f}.")
        except FundsException as error:
            # handle cases of insufficient funds using our exception class
            print(f"\nAttempting to withdraw £{amount:.2f}...\n{error}")