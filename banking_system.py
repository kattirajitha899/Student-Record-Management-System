
class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self._balance = balance
        self.transactions = ["Account created"]

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self._balance += amount
        self.transactions.append(f"Deposited: Rs. {amount:.2f}")
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            self.transactions.append(
                f"Withdrawn: Rs. {amount:.2f}"
            )
            print("Withdrawal successful!")

    def show_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: Rs. {self._balance:.2f}")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(Account):
    def __init__(self, name, account_number, balance=0):
        super().__init__(name, account_number, balance)
        self.account_type = "Savings"


def main():
    accounts = {}

    while True:
        print("\n=== PYTHON BANKING SYSTEM ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            number = input("Enter account number: ").strip()

            if not number:
                print("Account number cannot be empty.")
            elif number in accounts:
                print("This account already exists.")
            else:
                name = input("Enter account holder name: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                accounts[number] = SavingsAccount(name, number)
                print("Account created successfully!")

        elif choice in ("2", "3", "4", "5"):
            number = input("Enter account number: ").strip()
            account = accounts.get(number)

            if account is None:
                print("Account not found. Create an account first.")
                continue

            if choice == "2":
                try:
                    amount = float(input("Enter deposit amount: Rs. "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: Rs. "))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                account.show_balance()

            elif choice == "5":
                account.show_transactions()

        elif choice == "6":
            print("Thank you for using the banking system!")
            break

        else:
            print("Invalid option. Please choose 1 to 6.")


if __name__ == "__main__":
    main()

