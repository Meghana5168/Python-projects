import logging as lg
lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format="[%(asctime)s - %(levelname)s]- %(message)s"

)

#total operators 
operators=(
    "1. Balance\n",
    "2. withdraw\n",
    "3. deposite\n",
    "4. transfer\n",
    "5. History\n",
    "6. Exit\n"
)
#user table 
user_table={
    1234:["Meghana","meghana@gmail.com",1000],
    12345:["megha","megha@gmail.com",25000],
    2345:["sujatha","suja@gmail.com",3000]

}
#account table
account_table={
    1234:234,
    12345:234,
    2345:6158
    }
#checking valid user
def valid_user(account_no:int,pin:int):
    if account_no in account_table:
        if account_table[account_no]==pin:
            lg.info("User successfully login")
            print("User successfully login")
            return True
        else:
            lg.warning("Please check the pin")
            print("Please check the pin")
            return False
    else:
        lg.warning("Please check the user credentials")
        print("Please check the user credentials")
        return False
# balance function
def balance(account_no:int):
    lg.info("user in balance page")
    if account_no in user_table:
        amount=user_table[account_no][2]
        lg.info(f"{account_no} user current balence is {amount}")
        print(f"{account_no} user current balence is {amount}")
    else:
        lg.warning("User not found")
        print("User not found")

#withdraw function
def withdraw(account_no:int):
    lg.info("user in withdraw page")
    amount=user_table[account_no][2]
    withdraw_amount=int(input("Please enter withdraw amount : "))
    if amount>=withdraw_amount:
        user_table[account_no][2]-=withdraw_amount
        lg.info(f"{withdraw_amount} withdraw successful and current balance is {user_table[account_no][2]}")
        print(f"{withdraw_amount} withdraw successful and current balance is {user_table[account_no][2]}")
    else:
        lg.info("Insufficent amount")
        print("Insufficient amount")
# deposite function
def deposite(account_no:int):
    lg.info("user in deposite page")
    deposite_amount=int(input("Please enter deposit amount : "))
    if account_no in user_table:
        user_table[account_no][2]+=deposite_amount
        lg.info(f"{deposite_amount} is deposited successful and current balance is {user_table[account_no][2]}")
        print(f"{deposite_amount} is deposited successful and current balance is {user_table[account_no][2]}")
    else:
        lg.warning("User not found")
        print("User not found")
# transfer function
def transfer(account_no:int):
    lg.info("user in transfer page")
    recevier_account=int(input("Enter Recevier account number : "))
    amount=int(input("Enter amount "))
    lg.info(f"Recevier account is {recevier_account} and amount is {amount}")
    current_amount=user_table[account_no][2]
    if recevier_account in user_table:
        if current_amount>=amount:
            #amount updatetion in users table
            user_table[account_no][2] -= amount
            user_table[recevier_account][2]+=amount
            lg.info(f"{amount} transfer successfully and current balence is {user_table[account_no][2]}")
            print(f"{amount} transfer successfully and current balence is {user_table[account_no][2]}")
        else:
            lg.warning("Insufficent amount")
            print("Insufficent amount")
    else:
        lg.warning(f'{recevier_account} not found')
        print(f'{recevier_account} not found')
# history function
def history(account_no:int):
    lg.info("user in history page")
    print("Hitory function is under development process")
#exit function
def exit_fun():
    lg.info("user in history page")
    print("successfully exited, thankyou for using codegnan online bank services")
    return True

#choose operators
def choose_operation(account_no,choice):
    lg.info(f"select operation is {operators[choice-1]}")
    if choice ==1:
        balance(account_no=account_no)
    elif choice ==2:
        withdraw(account_no=account_no)
    elif choice ==3:
        deposite(account_no=account_no)
    elif choice ==4:
        transfer(account_no=account_no)
    elif choice ==5:
        history(account_no=account_no)
    elif choice ==6:
        val = exit_fun()

if __name__=="__main__":
    print("Welcome to the online codegnan Banking")
    lg.info("Welcome to the online codegnan Banking")
    account_no=int(input("Please enter account_no number"))
    pin=int(input("Please enter your pin"))
    lg.info("user credentials are {account_no}and {pin}")
    if valid_user(account_no=account_no,pin=pin):
        print(*operators)
        lg.info(operators)
        choice =int(input("Please select your opteration(1-6):"))
        choose_operation(account_no,choice)

    else:
        lg.warning("User not found,please check your credentials")
        print("User not found,please check your credentials")




