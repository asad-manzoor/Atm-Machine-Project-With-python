"""
SS Bank
"""
import random
import os

accounts_data = dict()


class Account:
    """
    Account Class
    """
    first_name: str = None
    last_name: str = None
    phone: str = None
    account_no: str = None
    pin: int = None
    balance: float = 0

    def __init__(self, first_name, last_name, phone, balance=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.account_no = self.generate_account_number
        self.pin = self.set_account_pin(self.pin)
        self.balance = balance

    def set_account_pin(self, pin):
        self.pin = pin
        return self.pin

    @property
    def generate_account_number(self):
        """a"""
        range_start = 10 ** (5 - 1)
        range_end = (10 ** 5) - 1
        number = str(random.randint(range_start, range_end))
        account_no = '1234' + number
        return account_no

    def confirm_detail(self):
        """a"""
        print("Please confirm your details:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name Number: {self.last_name}")
        print(f"phone no: {self.phone}\n")

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.first_name.upper()} {self.last_name.upper()}")
        print(f"Account Number: {self.account_no}")
        print(f"Available balance: {self.balance}\n")

    def deposit(self, amount):
        amount = amount
        self.balance = self.balance + amount
        print("Current account balance: ", self.balance)

    def withdraw(self, amount):
        amount = amount
        if amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} only.")
            print("Try with lesser amount than balance.")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawal successful!")
            print("Current account balance:", self.balance)


def pin_code() -> int:
    """a"""
    while True:
        pin = str(input('Please choose a 4 digit pin code:'))
        while len(pin) != 4 or (pin.isalpha()) or (not pin.isdigit()):
            print("please enter only 4 digits")
            pin = str(input('Please choose your pin code:'))
        re_pin = str(input('Please confirm your pin code:'))
        while len(re_pin) != 4 or (re_pin.isalpha()) or (not re_pin.isdigit()):
            print("please enter only 4 digits")
            re_pin = str(input('Please confirm your pin code:'))
        if pin != re_pin:
            print("write same pin code try again!")
            continue
        elif pin == re_pin:
            pin = int(re_pin)
            return pin
        break


def display_main_menu() -> str:
    """
    This function should only display the main menu, get input and return the choice
    return: create_account, view_account, exit
    """
    global choice
    print("Select your choice")
    print("1. create_account")
    print("2. view_account")
    print("3. exit")
    while True:
        try:
            option = int(input('Enter your choice: '))
            if option == 1:
                choice = "create_account"
                break
            elif option == 2:
                choice = "view_account"
                break
            elif option == 3:
                choice = "exit"
                break
            else:
                print("Invalid choice!-----Enter [1 to 3]")
                continue
        except ValueError:
            print("Invalid choice!-----Enter [1 to 3]")
            continue
    return choice


def start_account_creation() -> dict:
    """Get User Account Creation input and return a dict"""
    while True:
        clear()
        print("Welcome to SS Bank's Account Creation.")
        while True:
            first_name = str(input('Enter your first name: '))
            if not first_name.isalpha():
                print('Incorrect')
                continue
            else:
                break
        while True:
            last_name = str(input('Enter your last name: '))
            if not last_name.isalpha():
                print('Incorrect please enter only letters')
                continue
            else:
                break
        phone = str(input('Enter your Phone number:'))
        while len(phone) != 10 or (phone.isalpha()) or (not phone.isdigit()):
            print("Incorrect please enter only 10 digits")
            phone = str(input('Enter your Phone number:'))
        account = Account(first_name, last_name, phone)
        account.confirm_detail()
        press = input("Press Y to continue or C to change:")
        if press == "c" or press == "C":
            continue
        elif press == "y" or press == "Y":
            clear()
            print(f"Account Successfully created. Your account number is {account.account_no}")
            pin = pin_code()
            account.set_account_pin(pin)
            accounts_data[account.account_no] = {"first name": account.first_name,
                                                 "last name": account.last_name,
                                                 "phone no": account.phone,
                                                 "pin": account.pin,
                                                 "balance": account.balance}
            print("your account setup has been completed......")
            return accounts_data

        else:
            print("please press valid button!")
            continue


def account_match():
    """Account match"""

    while True:
        clear()
        account_number = str(input('Please enter your account number:'))
        while len(account_number) != 9 or (account_number.isalpha()) or (not account_number.isdigit()):
            print("Not a 9 digit account number")
            account_number = str(input('Enter your account number:'))
        if accounts_data.get(account_number):
            pin_number = str(input('Please enter your pin number:'))
            while len(pin_number) != 4 or (pin_number.isalpha()) or (not pin_number.isdigit()):
                print("Not a 4 digit pin number try again")
                pin_number = str(input('Enter your Pin number:'))
            match_pin = int(pin_number)
            accounts_data.get(account_number)
            pin_find = accounts_data.get(account_number).get("pin")
            find_pin = int(pin_find)
            if match_pin == find_pin:
                first_name = accounts_data.get(account_number).get("first name")
                last_name = accounts_data.get(account_number).get("last name")
                phone = accounts_data.get(account_number).get("phone")
                balance = accounts_data.get(account_number).get("balance")
                access_account = Account(first_name, last_name, phone, balance)
                clear()
                print(f"Welcome to SS Bank, Your current account balance is {balance}")
                print("Access Account")
                while True:
                    print("\n1. Account Detail\n2. Deposit\n3. Withdraw\n4. Change pin\n5. Exit")
                    option = int(input("Enter 1, 2, 3 4 or 5:"))
                    if option == 1:
                        clear()
                        access_account.account_detail()
                    elif option == 2:
                        clear()
                        amount = int(input("How much you want to deposit:"))
                        access_account.deposit(amount)
                    elif option == 3:
                        clear()
                        amount = int(input("How much you want to withdraw:"))
                        access_account.withdraw(amount)
                    elif option == 4:
                        print("---------Change pin code")
                        print(accounts_data)
                        new_pin = pin_code()
                        update_pin=accounts_data.get(account_number)
                        if accounts_data.get(account_number):
                            update_pin.update({"pin": new_pin})
                    elif option == 5:
                        run()

            else:
                print("Account number and pin code incorrect please try again!")
        else:
            print("Not Access")
            continue


def run():
    while True:
        clear()
        print("Welcome to SS Bank.")
        selected_option = display_main_menu()
        # check selected option to see if is create_account, view_account or exit
        if selected_option == "create_account":
            user_data: dict = start_account_creation()
        elif selected_option == "view_account":
            account_match()
        else:
            break
    exit(0)


if __name__ == "__main__":
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    run()
