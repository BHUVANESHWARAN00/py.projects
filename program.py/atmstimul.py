class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self._pin = pin
        self.balance = balance
        self.transactions = []  
    def check_pin(self, entered_pin):
        return entered_pin == self._pin
 
    def check_balance(self):
        return self.balance
 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return True
        return False
 
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return True
        return False
 
    def get_transactions(self):
        return self.transactions
 
 
class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_account = None
 
    def add_account(self, account):
        self.accounts[account.account_number] = account
 
    def login(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.check_pin(pin):
            self.current_account = account
            return True
        return False
 
    def logout(self):
        self.current_account = None
 
    def get_balance(self):
        if self.current_account:
            return self.current_account.check_balance()
 
    def deposit(self, amount):
        if self.current_account:
            return self.current_account.deposit(amount)
 
    def withdraw(self, amount):
        if self.current_account:
            return self.current_account.withdraw(amount)
 
    def transaction_history(self):
        if self.current_account:
            return self.current_account.get_transactions()
 
 
def main():
    atm = ATM()
 
    atm.add_account(Account("12345", "4321", 1000))
    atm.add_account(Account("67890", "9876", 500))
 
    print("Welcome to the ATM")
 
    while True:
        acct_num = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
 
        if atm.login(acct_num, pin):
            print("Login successful!")
            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transaction History")
                print("5. Logout")
 
                choice = input("Select an option: ")
 
                if choice == '1':
                    print(f"Current balance: ${atm.get_balance():.2f}")
 
                elif choice == '2':
                    amt = float(input("Enter deposit amount: $"))
                    if atm.deposit(amt):
                        print("Deposit successful.")
                    else:
                        print("Invalid amount.")
 
                elif choice == '3':
                    amt = float(input("Enter withdrawal amount: $"))
                    if atm.withdraw(amt):
                        print("Withdrawal successful.")
                    else:
                        print("Insufficient balance or invalid amount.")
 
                elif choice == '4':
                    history = atm.transaction_history()
                    if history:
                        print("Transaction History:")
                        for item in history:
                            print("-", item)
                    else:
                        print("No transactions yet.")
 
                elif choice == '5':
                    atm.logout()
                    print("Logged out.")
                    break
 
                else:
                    print("Invalid option. Try again.")
 
        else:
            print("Invalid account number or PIN.")
 
        cont = input("Do you want to try again? (y/n): ").lower()
        if cont != 'y':
            print("Thank you for using the ATM. Goodbye!")
            break
 
if __name__ == "__main__":
    main()
 