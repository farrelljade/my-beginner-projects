import json

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
        with open('account_names.json', 'r') as file:
            user_balance = json.load(file)
            print(f"\n{user_balance['acc_name']}: Account Balance: £{user_balance['balance']:.2f}")

    def deposit(self, amount):
        with open('account_names.json', 'r+') as file:
            user_deposit = json.load(file)
            user_deposit['balance'] += amount  # Update the balance
            file.seek(0)  # Move the file pointer to the beginning
            json.dump(user_deposit, file)  # Write the updated data back to the file
        return user_deposit['balance']  # Return the updated balance

    def withdraw(self, amount):
        with open('account_names.json', 'r+') as file:
            data = json.load(file)
            if data['balance'] >= amount:
                data['balance'] -= amount
                file.seek(0)
                json.dump(data, file)
                file.truncate()  # Truncate any extra content
            else:
                raise FundsException(f"Insufficient funds. Account balance: £{data['balance']}")

            return data['balance']

    def transfer(self, recipient, amount):
        with open('account_names.json', 'r+') as file:
            data = json.load(file)
            if data['balance'] >= amount:
                data['balance'] -= amount
                data['balance'] += amount
                file.seek(0)
                json.dump(data, file)
                file.truncate()
            else:
                raise FundsException(f"Insufficient funds. Account balance: £{data['balance']}")

class UserInterface(BankAccount):
    def __init__(self, acc_name, balance):
        super().__init__(acc_name, balance)
        self.load_data()

    def load_data(self):
        try:
            with open('account_names.json', 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:  
            self.data = {}
        except json.JSONDecodeError:
            self.data = {}
    
    # whenever a new bank account created its added to a separate json file
    def create_account(self, acc_name):
        # if acc_name not in self.data:
        with open('account_names.json', 'r') as file:
            existing_data = json.load(file)
            if acc_name not in self.data:

                self.data = BankAccount(acc_name, 0).__dict__
                existing_data.update(self.data)

        with open('account_names.json', 'w') as file:
            json.dump(existing_data, file)
    # else:
    #     print(f"Account with {self.acc_name} already exists.")
    #     return self.data[acc_name]  # return the bank account already stored

        # with open('account_names.json', 'w') as file:
        #     json.dump(self.data, file)
        
    def back_to_menu(self):
        user_choice = input("\n1. Main menu\n2. Return card\nEnter your choice: ").lower()
        if user_choice == "2" or user_choice == "return card":
            raise ReturnCard
        
    def switch_acc(self):
        switched_acc = input("What account to switch to: ")
        with open('account_names.json', 'r') as file:
            data = json.load(file)
            if switched_acc in data:
                self.acc_name = switched_acc
                self.bank_menu(self.acc_name)
            else:
                print(f"{switched_acc} not found.")

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
            
            if user_choice in ["1", "check balance", "checkbalance"]:
                self.check_balance()
            elif user_choice in ["2", "deposit"]:
                amount = int(input("\nDeposit amount: "))
                self.deposit(amount)
                print(f"Depositing £{amount:.2f}...\nDeposit complete.")
            elif user_choice in ["3", "withdrawal", "withdraw"]:
                amount = int(input("\nWithdrawal amount: "))
                try:
                   self.withdraw(amount)
                   print(f"Withdrawal complete.")
                   self.check_balance()
                except FundsException as error:
                    print(f"Attempting to withdraw £{amount}...\n{error}")
            elif user_choice in ["4", "transfer"]:
                recipient_name = input("\nWhose account to transfer to: ")
                amount = float(input("\nTransfer amount: "))
                try:
                    self.transfer(recipient_name, amount)
                    with open('account_names.json', 'r') as file:
                        data = json.load(file)
                        print(f"Transfer complete.\n{acc_name}'s balance: £{data['balance']:.2f}")
                        print(f"{recipient_name}'s balance: £{data[recipient_name]['balance']:.2f}")
                except FundsException as error:
                    print(f"Attempting to transfer £{amount}...\n{error}")
            elif user_choice in ["6", "switch account", "switchaccount"]:
                self.switch_acc()

ui = UserInterface(acc_name=None, balance=0)

while True:
    acc_name = input("\nEnter your account name (or press Enter to exit): ")
    if not acc_name:
        break
    if acc_name:
        ui.create_account(acc_name)
        
    while True:
        try:
            ui.bank_menu(acc_name)
            ui.back_to_menu()
        except ReturnCard:
            print("\nReturning card...")
            break