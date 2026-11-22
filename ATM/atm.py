balance = 10000
pin = 1234

print("===== WELCOME TO ATM =====")

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == 3:
            amount = int(input("Enter amount: "))
            balance = balance + amount
            print("Deposit Successful!")
            print("New Balance:", balance)

        elif choice == 4:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Wrong PIN!")