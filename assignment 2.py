users=[0]
print(users)
while True:
    print("1.User\n2.Administrator\n3.Exit")
    c=int(input("Enter you choice:"))
    admistrator="admin123"
    if c==1:
        acc_num=input("Enter your account number:")
        if acc_num in users:
            while True:
                print("1.Deposit \n2.Withdraw\n3.View account details\n4.Logout")
                choice=int(input("Enter your choice:"))
                if choice==1:
                    deposit=int(input("Enter amount to deposit:"))
                    if deposit<=0:
                        print("Invalid amount")
                    else:
                        print("Amount deposited")
                        new_balance=balance+deposit
                        users.append({"Balance":[new_balance]})
                elif choice==2:
                    withdraw=int(input("Enter amount to withdraw:"))
                    if withdraw<=0:         
                        print("Invalid amount")
                    else:
                        print("Amount wihdraw")
                        withdraw_balance=balance-withdraw
                        users.append({"Balance":[withdraw_balance]})
                elif choice==3:
                    print(users)
                elif choice==4:
                    print("Logging out.....")
                    break
                else:
                    print("Invalid choice")
        else:
                print("Account not found")
    elif c==2:
        ad=input("Enter your administrator password:")
        if admistrator==ad:
            while True:
                print("1.Create account\n2.Log out")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    acc_name=input("Enter account name:")
                    acc_num=input("Enter your account number:")
                    balance=int(input("Enter your account balance:"))
                    users.append({"Name":acc_name,"Number":acc_num,"Balance":balance})
                    print("Account created")
                elif ch==2:
                    print("Logging out.....")
                    break
                else:
                    print("Invalid choice")
        else:
            print("Wrong password")
    elif c==3:
        print("Exiting banking system.....")
        break
    else:
        print("Invalid choice")