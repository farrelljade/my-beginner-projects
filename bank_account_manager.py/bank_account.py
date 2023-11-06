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
        # Display the current bank balance of the account holder
        print(f"\nYour current balance is: £{self.balance}")

    def deposit(self, deposit_amount):
        # deposit funds into the account and update the balance
        self.balance += deposit_amount
        print(f"\nDepositing £{deposit_amount:.2f}...\nDeposit complete.\nYour accout balanceis now: £{self.balance:.2f}.")

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
            print(f"\nWithdrawing £{amount:.2f}...")
            user_choice = input("Confirm withdrawal: ").lower()
            if user_choice in ["yes", "y"]:
                self.balance -= amount
                print(f"Withdrawal complete.\nYour account balance is now: £{self.balance:.2f}.")
            else:
                print(f"Withdrawal request cancelled.\nAccount balance: £{self.balance}")
        except FundsException as error:
            # handle cases of insufficient funds using our exception class
            print(f"\nAttempting to withdraw £{amount:.2f}...\n{error}")

    def transfer(self, user, amount):
        try:
            # first check enough funds to make the transfer
            self.enough_funds(amount)
            print(f"\nTransferring £{amount:.2f} to {user.acc_name}'s account.")
            user_choice = input("Confirm Transfer: ").lower()
            if user_choice in ["yes", "y"]:
                user.balance += amount  # update the recipients account
                self.balance -= amount  # adjust senders account
                print(f"Transfer complete.\nYour account balance is now: £{self.balance:.2f}")
            else:
                print(f"Transfer cancelled.\nAccount balance: {self.balance}")
        except FundsException as error:
            # handle cases of insufficient funds using our exception class
            print(f"Attempting to transfer £{amount:.2f} to {user}' account...\n{error}.")

class SavingsAccount(BankAccount):

    def deposit(self, amount):
        self.interest = amount * 1.10
        self.balance += self.interest
        print(f"\nDepositing £{amount:.2f}...\nDeposit complete.\nYour accout balance is now: £{self.balance:.2f}.")

class CashIsaAccount(SavingsAccount):
    def __init__(self, acc_name, balance):
        super().__init__(acc_name, balance)
        self.withdraw_fee = 5

    def withdraw(self, amount):
        try:
            self.enough_funds(amount)            
            print(f"\nWithdrawal amount: £{amount:.2f}.")
            user_choice = input(f"£{self.withdraw_fee} fee for this withdrawal. Do you accept the fee: ").lower()
            if user_choice in ["yes", "y"]:
                self.balance -= (amount + self.withdraw_fee)
                print(f"Withdrawal complete.\nYour account balance is now: £{self.balance:.2f}.")
            else:
                print(f"Withdrawal request cancelled.\nAccount balance: £{self.balance}")
        except FundsException as error:
            # handle cases of insufficient funds using our exception class
            print(f"\nAttempting to withdraw £{amount:.2f}...\n{error}")