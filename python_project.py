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
            "transactions" : [f"+{initial_deposit}Rs"],
        }
        print(f"Account created! Thanks for trusting us.Your account number is {acc_no}")  # print stt

    def displayAccounts(self):  # Display all accounts ("Good for the bank to manage all bank cuctomers")
        print("\nAvailable Accounts:")
        for acc_no, details in self.accounts.items():
            print(f"Account No: {acc_no}, Name: {details['name']}, Balance: {details['balance']}")  # print stt

    def getAccountDetails(self, acc_no):  # Display customer account details
        if acc_no in self.accounts:  # conditional statements
            return self.accounts[acc_no]
        else:
            print("Account not found!")
            return None

if __name__ == "__main__":
    swizzBank = Bank()
    
    # swizzBank.displayAccounts()

    while True:  # for menu driven program use a infinte loop
        print('''\n|=|=|=| Welcome to Swizz Bank |=|=|=|
              1. Create Account
              2. Deposit Money
              3. Withdraw Money
              4. Transfer Money
              5. View Account details
              6. Exit''')

        choice = int(input("Enter your choice : "))

#Conditional statements

        if choice == 1:
            name = input("Enter a your name : ")  #user input
            deposit = float(input("Enter initial deposit : "))  #user input  #user input

            swizzBank.createAccount(name, deposit)  #function call

        elif choice == 2:
            acc_no = input("Enter your account number : ")  #user input

            if acc_no in swizzBank.accounts:
                amount = float(input("Enter deposit amount : "))  #user input
                swizzBank.accounts[acc_no]["balance"] += amount
                swizzBank.accounts[acc_no]["transactions"].append(f"+{amount} Rs")
                print("Deposit successful!")

            else:
                print("Account not found!")

        elif choice == 3:
            acc_no = input("Enter your account number : ")  #user input

            if acc_no in swizzBank.accounts:
                amount = float(input("Enter withdrawal amount : "))  #user input
                if amount > swizzBank.accounts[acc_no]["balance"]:
                    print("Insufficient balance!")
                else:
                    swizzBank.accounts[acc_no]["balance"] -= amount
                    swizzBank.accounts[acc_no]["transactions"].append(f"-{amount} Rs")
                    print("Withdrawl successful!")

            else:
                print("Account not found!")

        elif choice == 4:
            sender_acc = input("Enter your account number : ")  #user input
            receiver_acc = input("Enter receiver's account number : ")  #user input
            amount = float(input("Enter transfer amount : "))  #user input

            if sender_acc in swizzBank.accounts and receiver_acc in swizzBank.accounts:
                if amount > swizzBank.accounts[sender_acc]["balance"]:
                    print("Insufficient balance!")
                else:
                    swizzBank.accounts[sender_acc]["balance"] -= amount
                    swizzBank.accounts[sender_acc]["transactions"].append(f"-{amount}Rs (Transfer to {receiver_acc})")
                    swizzBank.accounts[receiver_acc]["balance"] += amount
                    swizzBank.accounts[receiver_acc]["transactions"].append(f"+{amount}Rs (Transfer from {sender_acc})")
                    
                    print("Transfer successful!")
                
            else:
                print("One or both accounts not found!")
                
        elif choice == 5:
            acc_no = input("Enter account number : ")  #user input
            details = swizzBank.getAccountDetails(acc_no)  #function call
            if details:
                print(f"Name : {details['name']}, Balance : {details['balance']} Rs")
                print("Transactions :", details["transactions"])
                
        elif choice == 6:
            print("Thanks for using Swizz Bank!")
            exit()
        
        else:
            print("Invalid option! Try again.")