"""
Banking System Project

This Python program implements a simple banking system with two classes:
- `BankAccount`: Represents a bank account and provides basic account operations.
- `UserInterface`: Handles user input and output, as well as managing multiple accounts.

The program allows users to create and manage bank accounts, check balances, make deposits,
withdrawals, and transfers between accounts. Each account is associated with an account
name and an initial balance.

Usage:
1. Create an account by entering an account name.
2. Access the account menu to perform various operations.
3. You can return to the main menu or return the card.
"""

class FundsException(Exception):
    pass

class ReturnCard(Exception):
    pass

class BankAccount:
    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise FundsException(f"Insufficient funds. Account balance: £{self.balance}")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
        else:
            raise FundsException(f"Insufficient funds. Account balance: £{self.balance}")
        
# Inheritance class        
class SavingAccount(BankAccount):
    def __init__(self, acc_name, balance):
        super().__init__(acc_name, balance)

    def deposit(self, amount):
        self.balance += (amount * 1.10)

# Inheritance class
class CashIsaAccount(SavingAccount):
    def __init__(self, acc_name, balance):
        super().__init__(acc_name, balance)
        self.service_fee = 5

    def withdraw(self, amount):
        if self.balance >= amount + self.service_fee:
            self.balance -= amount + self.service_fee
        else:
            raise FundsException(f"Insufficient funds. Account balance: £{self.balance}")

class UserInterface:
    def __init__(self):
        self.user_accounts = {}
        self.recip_acc = None
    
    # whenever a new bank account created its added to the dict
    def create_account(self, acc_name, acc_type):
        if acc_name not in self.user_accounts:
            self.user_accounts[acc_name] = acc_type
        else:
            print(f"Account with {acc_name} already exists.")
            return self.user_accounts[acc_name]  # return the bank account already stored
        
    def back_to_menu(self):
        user_choice = input("\n1. Main menu\n2. Return card\nEnter your choice: ").lower()
        if user_choice == "2" or user_choice == "return card":
            raise ReturnCard
        
    def switch_acc(self):
        user_acc = input("\nWhat account to switch to: ")
        if user_acc in self.user_accounts:
            self.bank_menu(user_acc)
        else:
            print(f"{user_acc} not found.")

    def bank_menu(self, acc_name):
        while True:
            print("\nOPTIONS:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Transfer")
            print("5. Return Card")
            print("6. Switch Account")

            user_choice = input("Enter your choice: ").lower()
            if user_choice in ["5", "return card", "returncard"]:
                raise ReturnCard
            
            account = self.user_accounts.get(acc_name)
            
            if user_choice in ["1", "check balance", "checkbalance"]:
                print(f"\n{acc_name}, your current balance is: £{account.check_balance():.2f}")
            elif user_choice in ["2", "deposit"]:
                amount = int(input("\nDeposit amount: "))
                account.deposit(amount)
                print(f"Depositing £{amount:.2f}...\nDeposit complete.\n{acc_name}'s balance is: £{account.check_balance():.2f}")
            elif user_choice in ["3", "withdrawal", "withdraw"]:
                amount = int(input("\nWithdrawal amount: "))
                try:
                   account.withdraw(amount)
                   print(f"Withdrawal complete. {acc_name}'s balance is now: £{account.check_balance():.2f}")
                except FundsException as error:
                    print(f"Attempting to withdraw £{amount}...\n{error}")
            elif user_choice in ["4", "transfer"]:
                recipient_name = input("\nWhose account to transfer to: ")
                recipient = self.user_accounts.get(recipient_name)  # look up if account in dict
                if recipient:
                    amount = float(input("\nTransfer amount: "))
                    try:
                        account.transfer(recipient, amount)
                        print(f"Transfer complete.\n{acc_name}'s balance is now: £{account.check_balance():.2f}")
                        print(f"{recipient_name}'s balance is now: £{recipient.balance:.2f}")
                    except FundsException as error:
                        print(f"Attempting to transfer £{amount}...\n{error}")
                else:
                    print("Recipient not found.")
            elif user_choice in ["6", "switch account", "switchaccount"]:
                self.switch_acc(self.recip_acc)

ui = UserInterface()

while True:
    acc_name = input("\nEnter your account name (or press Enter to exit): ")
    if not acc_name:
        break

    user_account = input("What type of account would you like to setup:\n1. Bank Account\n2. Savings Account\n3. Cash ISA Account\n\n").lower()

    if user_account in ["1", "bank account", "bankaccount"]:
        ui.create_account(acc_name, BankAccount(acc_name, 0))
    elif user_account in ["2", "savings acoount", "savingsaccount"]:
        ui.create_account(acc_name, SavingAccount(acc_name, 0))
    elif user_account in ["3", "cash isa account", "cashisaaccount"]:
        ui.create_account(acc_name, CashIsaAccount(acc_name, 0))

    while True:
        try:
            ui.bank_menu(acc_name)
            ui.back_to_menu()
        except ReturnCard:
            print("\nReturning card...")
            break