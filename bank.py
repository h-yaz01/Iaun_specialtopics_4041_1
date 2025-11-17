
accounts = {}

count = int(input("How many bank accounts do you want to create? "))

for i in range(count):
    print(f"\nAccount number {i+1}:")
    name = input("Account holder name: ")
    balance = float(input("Initial balance: "))
    accounts[name] = balance

while True:
    print("\n===== Banking Menu =====")
    print("1. Show all account balances")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Accounts above average balance")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- All Accounts ---")
        for name, balance in accounts.items():
            print(name, ":", balance)

    elif choice == "2":
        acc = input("Account name for deposit: ")
        if acc in accounts:
            amount = float(input("Deposit amount: "))
            accounts[acc] += amount
            print("Deposit successful.")
        else:
            print("Account not found.")

    elif choice == "3":
        acc = input("Account name for withdrawal: ")
        if acc in accounts:
            amount = float(input("Withdrawal amount: "))
            if accounts[acc] >= amount:
                accounts[acc] -= amount
                print("Withdrawal done.")
            else:
                print("Not enough balance.")
        else:
            print("Account not found.")

    elif choice == "4":
        avg = sum(accounts.values()) / len(accounts)
        print("Average balance:", avg)
        print("Accounts above average:")
        for name, balance in accounts.items():
            if balance > avg:
                print(name, ":", balance)

    elif choice == "5":
        print("Exiting the program...")
        break

    else:
        print("Invalid option, try again.")