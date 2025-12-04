users = []
while True:
    print("---------MAIN MENU---------")
    print("1.User\n2.Administrator\n3.Exit")
    c = int(input("Enter your choice:"))
    administrator = "admin123"
    if c == 1:
        acc_num = input("Enter your account number:")
        found_user = None
        for u in users:
            if u["Number"] == acc_num:
                print("Account found")
                found_user = u
                break
        if found_user is None:
            print("Account not found")
            continue
        while True:
            print("---------USER MENU---------")
            print("1.Deposit \n2.Withdraw\n3.View account details\n4.Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                deposit = int(input("Enter amount to deposit:"))
                if deposit <= 0:
                    print("Invalid amount")
                else:
                    found_user["Balance"] += deposit
                    print("Amount deposited successfully")
            elif choice == 2:
                withdraw = int(input("Enter amount to withdraw:"))
                if withdraw <= 0:
                    print("Invalid amount")
                else:
                    found_user["Balance"] -= withdraw
                    print("Amount withdrawn successfully")
            elif choice == 3:
                print(found_user)
            elif choice == 4:
                print("Logging out.....")
                break
            else:
                print("Invalid choice")
    elif c == 2:
        while True:
            ad = input("Enter your administrator password:")
            if administrator == ad:
                while True:
                    print("---------ADMINISTRATOR MENU---------")
                    print("1.Create account\n2.Log out")
                    ch = int(input("Enter your choice:"))
                    if ch == 1:
                        acc_name = input("Enter account name:")
                        acc_num = input("Enter your account number:")
                        balance = int(input("Enter your account balance:"))
                        users.append({"Name": acc_name,"Number": acc_num,"Balance": balance})
                        print("Account created")
                    elif ch == 2:
                        print("Logging out.....")
                        break
                    else:
                        print("Invalid choice")
                break
            else:
                print("Wrong password")
                print("Try again")
    elif c == 3:
        print("Exiting banking system.....")
        break
    else:
        print("Invalid choice")
