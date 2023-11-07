# define an exception class to deal with insufficient funds. (- balances)
class FundsException(Exception):
    pass

class BankAccount:
    user_accounts = {}
    # initialise bank account with account name and balance
    def __init__(self, acc_name, balance=0):
        self.acc_name = acc_name
        self.balance = balance
        self.user_accounts[acc_name] = self  # add the instance to user_account dict
        print(f"\nBank account created for: {acc_name}.")
        self.bank_menu()
            
    
    # Bank menu added for more interaction
    def bank_menu(self):
        user_choice = input("\nOPTIONS:\n1. Check Balance\n2. Deposit\n3. Withdrawal\n4. Transfer\n5. Return Card\n\n").lower()
        if user_choice in ["5", "return card", "returncard"]:
            return
        elif user_choice in ["1", "check balance", "checkbalance"]:
            self.check_balance()
        elif user_choice in ["2", "deposit"]:
            self.deposit()
        elif user_choice in ["3", "withdrawal"]:
            self.withdraw()
        elif user_choice in ["4", "transfer"]:
            self.transfer()
    
    # Added function for user to go back to main menu or exit
    def back_to_menu(self):
        user_choice = input("\n1. Main menu\n2. Return card\n\n").lower()
        if user_choice in ["1", "main menu", "mainmenu"]:
            return self.bank_menu()
        else:
            return
    
    # Display the current bank balance of the account holder
    def check_balance(self):
        print(f"\n{self.acc_name}, your current balance is: £{self.balance:.2f}")
        user_choice = input("1. Back to menu\n2. Return card\n\n").lower()
        if user_choice == "1":
            self.bank_menu()
        else:
            return
    
    # Deposit funds into the account and update bank balance
    def deposit(self):
        user_choice = float(input("\nDeposit amount: "))
        self.balance += user_choice
        print(f"\nDepositing £{user_choice:.2f}...\nDeposit complete.\n{self.acc_name}'s balance is now: £{self.balance:.2f}.")
        self.back_to_menu()

    # Function to check enough funds before carrying out Withdrawals or Transfers
    def enough_funds(self, amount):
        if self.balance >= amount:
            return
        else:
            raise FundsException(f"Insufficient funds.\nAccount balance: £{self.balance:.2f}.")
    
    # Withdraw function. Checks if enough funds in account before withdrawing
    def withdraw(self):
        withdraw_amount = 0
        try:
            user_amount = input("\nWithdrawal amount:\n1. £10\n2. £20\n3. £50\n4. £100\n5. Other amount\n6. Return to menu\n\n")
            if "." in user_amount:
                print("Only £10 and £20 notes available.")
                self.withdraw()
            elif user_amount == "1":
                withdraw_amount = 10
            elif user_amount == "2":
                withdraw_amount = 20
            elif user_amount == "3":
                withdraw_amount = 50
            elif user_amount == "4":
                withdraw_amount = 100
            elif user_amount == "5":
                withdraw_amount = int(input("How much do you want to withdraw: "))
            elif user_amount in ["6", "return to menu", "returntomenu"]:
                return self.bank_menu()
            self.enough_funds(withdraw_amount)
            print(f"\nWithdrawing £{withdraw_amount:.2f}...")
            user_choice = input("Confirm withdrawal: ").lower()
            if user_choice in ["yes", "y"]:
                self.balance -= withdraw_amount
                print(f"Withdrawal complete.\n{self.acc_name}'s account balance is now: £{self.balance:.2f}.")
                self.back_to_menu()
            else:
                print(f"Withdrawal request cancelled.\n{self.acc_name}'s account balance: £{self.balance}")
        except FundsException as error:
            # handle cases of insufficient funds using our exception class
            print(f"\nAttempting to withdraw £{withdraw_amount:.2f}...\n{error}")
            self.withdraw()
    
    # Transfer function using a dict (user_accounts) to check recipient has a bank account
    def transfer(self):
        user_amount = int(input(f"\nHi {self.acc_name}. How much do you want to transfer amount: "))
        recipient_name = input("Whose account to transfer to: ")
        recipient = self.user_accounts.get(recipient_name)
        if recipient is not None:  # check in user is in the dict
            try:
                self.enough_funds(user_amount)
                print(f"\nTransferring £{user_amount:.2f}...")
                user_choice = input("Confirm transfer: ").lower()
                if user_choice in ["yes", "y"]:
                    recipient.balance += user_amount
                    self.balance -= user_amount
                    print(f"Transfer complete.\nYour account balance is now: £{self.balance:.2f}.")
                    self.back_to_menu()
                
                else:
                    print(f"Transfer cancelled.\nAccount balance: {self.balance}")
            except FundsException as error:
            # handle cases of insufficient funds using our exception class
                print(f"Attempting to transfer £{user_amount:.2f} to {recipient_name}'s account...\n{error}.")
        else:
            print("Recipient not found.")

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