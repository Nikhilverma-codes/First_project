# Bank Management System


# creates class Bank
class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store all accounts

    def createAccount(self, name, initial_deposit):  # Create account method
        acc_no = str(1001 + len(self.accounts))  # Generate a unique account number
        
        # Create cccount dictionary
        self.accounts[acc_no] = { 
            "name" : name,
            "balance" : initial_deposit,
            "transactions" : [f"+{initial_deposit}"],
        }
        print(f"Account created! Your account number is {acc_no}")

    def displayAccounts(self):  # Display all accounts ("Good for the bank to manage all bank cuctomers")
        print("\nAvailable Accounts:")
        for acc_no, details in self.accounts.items():
            print(
                f"Account No: {acc_no}, Name: {details['name']}, Balance: {details['balance']}"
            )

    def getAccountDetails(self, acc_no):  # Display customer account details
        if acc_no in self.accounts:
            return self.accounts[acc_no]
        else:
            print("Account not found!")
            return None

# creates class Account
class Account:
    def __init__(self, name, initial_balance):  # Constructor takes attributes name & inital balance
        self.name = name
        self.balance = initial_balance
        self.transactions = [f"+{initial_balance}"]

    def deposit(self, amount):  #
        self.balance += amount
        self.transactions.append(f"+{amount}")
        print(f"{amount} deposited successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"-{amount}")
            print(f"{amount} withdrawn successfully. New balance: {self.balance}")

    def transfer(self, amount, receiver_account):
        if amount > self.balance:
            print("Insufficient balance for transfer!")
        else:
            self.balance -= amount
            receiver_account.balance += amount
            self.transactions.append(f"-{amount} (Transfer to {receiver_account.name})")
            receiver_account.transactions.append(
                f"+{amount} (Transfer from {self.name})"
            )
            print(
                f"{amount} transferred to {receiver_account.name}. Your new balance: {self.balance}"
            )

    def getTransactionHistory(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)


# creates class Customer
class Customer:
    def requestDeposit(self):
        amount = float(input("Enter amount to deposit: "))
        return amount

    def requestWithdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        return amount

    def requestTransfer(self):
        receiver_account = input("Enter receiver's account number: ")
        amount = float(input("Enter amount to transfer: "))
        return receiver_account, amount


if __name__ == "__main__":
    swizzBank = Bank()
    # swizzBank.displayAccounts()

    while True:
        print('''\n|=|=|=| Welcome to State Bank of India |=|=|=|
              1. Create Account
              2. Deposit Money
              3. Withdraw Money
              4. Transfer Money
              5. View Account details
              6. Exit''')

        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter a your name : ")
            deposit = float(input("Enter initial deposit : "))

            swizzBank.createAccount(name, deposit)

        elif choice == 2:
            acc_no = input("Enter your account number")

            if acc_no in swizzBank.accounts:
                amount = float(input("Enter deposit amount : "))
                swizzBank.accounts[acc_no]["balance"] += amount
                swizzBank.accounts[acc_no]["transactions"].append(f"+{amount}")
                print("Deposit successful!")

            else:
                print("Account not found!")

        elif choice == 3:
            acc_no = input("Enter your account number : ")

            if acc_no in swizzBank.accounts:
                amount = float(input("Enter withdrawal amount : "))
                if amount > swizzBank.accounts[acc_no]["balance"]:
                    print("Insufficient balance!")
                else:
                    swizzBank.accounts[acc_no]["balance"] -= amount
                    swizzBank.accounts[acc_no]["transactions"].remove(f"-{amount}")
                    print("Withdrawl successful!")

            else:
                print("Account not found!")

        elif choice == 4:
            sender_acc = input("Enter your account number : ")
            receiver_acc = input("Enter receiver's account number")
            amount = float(input("Enter transfer amount : "))

            if sender_acc in swizzBank.accounts and receiver_acc in swizzBank.accounts:
                if amount > swizzBank.accounts[sender_acc]["balance"]:
                    print("Insufficient balance!")
                else:
                    swizzBank.accounts[sender_acc]["balance"] -= amount
                    swizzBank.accounts[sender_acc]["transactions"].append(
                        f"-{amount} (Transfer to {receiver_acc})"
                    )
                    swizzBank.accounts[receiver_acc]["balance"] += amount
                    swizzBank.accounts[receiver_acc]["transactions"].append(
                        f"+{amount} (Transfer from {sender_acc})"
                    )
                    print("Transfer successful!")
                
            else:
                print("One or both accounts not found!")
                
        elif choice == 5:
            acc_no = input("Enter account number : ")
            details = swizzBank.getAccountDetails(acc_no)
            if details:
                print(f"Name : {details['name']}, Balance : {details['balance']}")
                print("Transactions :", details["transactions"])
        elif choice == 6:
            print("Thanks for using Swizz Bank!")
            break
        else:
            print("Invalid option! Try again.")

