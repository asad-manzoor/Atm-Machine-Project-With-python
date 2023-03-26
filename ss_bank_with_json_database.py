"""ssbank"""

from random import randint
import json
import os


class Account:
    """a"""
    def __init__(self, first_name, last_name, phone, account_no, pin, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.account_no = account_no
        self.pin = pin
        self.balance = balance

    def storing_data(self):
        """a"""
        account_holder = {"account": self.account_no,
                          "pin": self.pin,
                          "first_name": self.first_name,
                          "last_name": self.last_name,
                          "phone": self.phone,
                          "balance": self.balance}
        with open('record.json', "r", encoding="utf-8") as file:
            data = json.load(file)
        data.append(account_holder)
        with open('record.json', "w", encoding="utf-8") as file:
            json.dump(data, file)

    def access_account(self):
        """a"""
        clear()
        while True:
            print(f"Welcome to SS Bank, Your current account balance is {self.balance}")
            print("Please choose one of the options:")
            print("1. Account Details")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change Pin")
            print("5. Exit")
            try:
                choose = int(input("Enter your option : "))
                clear()
                if choose == 1:
                    print("----Account Holder Detail")
                    print(f"First Name: {self.account_no}")
                    print(f"First Name: {self.first_name}")
                    print(f"Last Name: {self.last_name}")
                    print(f"phone no: {self.phone}")
                    print(f"balance: {self.balance}\n")
                    continue
                elif choose == 2:
                    print("----Deposit Money")
                    amount: int = int(input("How much you want to Deposit:"))
                    self.balance = self.balance + amount
                    print("Current account balance: ", self.balance)
                    with open("record.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        for i in data:
                            account_number = i.get("account")
                            if account_number == self.account_no:
                                i.update({"balance": self.balance})
                                with open('record.json', "w", encoding="utf-8") as file_update:
                                    json.dump(data, file_update)
                    continue
                elif choose == 3:
                    print("----Withdraw Money")
                    amount = int(input("How much you want to withdraw:"))
                    if amount > self.balance:
                        print("Insufficient fund!")
                        print(f"Your balance is {self.balance} only.")
                        print("Try with lesser amount than balance.")
                    else:
                        self.balance = self.balance - amount
                        print(f"{amount} withdrawal successful!")
                        print("Current account balance:", self.balance)
                    with open("record.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        for i in data:
                            account_number = i.get("account")
                            if account_number == self.account_no:
                                i.update({"balance": self.balance})
                                with open('record.json', "w", encoding="utf-8") as file_update:
                                    json.dump(data, file_update)
                    continue
                elif choose == 4:
                    print("---------Change pin code")
                    new_pin = pin_code()
                    with open("record.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        for i in data:
                            if account_number == self.account_no:
                                i.update({"pin": new_pin})
                                with open('record.json', "w", encoding="utf-8") as file_update:
                                    json.dump(data, file_update)
                    continue
                elif choose == 5:
                    menu()
                    break
                else:
                    print("Invalid choose!-----Enter [1 to 5]")
                    continue
            except ValueError:
                print("Invalid choose!-----Enter [1 to 5]")
                continue


def random(account):
    """a"""
    range_start = 10**(account-1)
    range_end = (10**account)-1
    return randint(range_start, range_end)


def firstname():
    """a"""
    while True:
        first_name = str(input('Enter your first name: '))
        if not first_name.isalpha():
            print('Enter only letters')
            continue
        else:
            break
    return first_name


def lastname():
    """a"""
    while True:
        last_name = input('Enter your last name: ')
        if not last_name.isalpha():
            print('Enter only letters')
            continue
        else:
            break
    return last_name


def phone_no():
    """a"""
    phone = str(input('Enter your Phone number:'))
    while len(phone) != 10:
        print('Error !')
        print("Not a 10 digit phone number")
        phone = str(input('Enter your Phone number:'))
    phone = int(phone)
    return phone


def pin_code():
    """A dummy docstring."""
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
        pin_code()
    elif pin == re_pin:
        pin = int(re_pin)
        return pin


def user_data():
    """a """
    clear()
    print("Welcome to SS Bank's Account Creation")
    first_name = firstname()
    last_name = lastname()
    phone = phone_no()
    print("Please confirm your details:")
    print(f"First Name: {first_name}")
    print(f"Last Name Number: {last_name}")
    print(f"phone no: {phone}\n")
    while True:
        press = input("Press Y to continue or C to change:")
        if press == "c" or press == "C":
            user_data()
            continue
        elif press == "y" or press == "Y":
            clear()
            account_no = '1234' + str(random(5))
            print(f"Account created successfully, Your account number is {account_no}")
            pin = pin_code()
            account = Account(first_name, last_name, phone, account_no, pin)
            account.storing_data()
            print("your account setup has been completed")
            break


def account_match():
    """Account match"""
    while True:
        clear()
        print("Welcome to SS Bank")
        accountno = str(input('Please enter your account number:'))
        while len(accountno) != 9 or (accountno.isalpha()) or (not accountno.isdigit()):
            print('Error !')
            print("Not a 9 digit account number")
            accountno = str(input('Enter your account number:'))
        pinno = str(input('Please enter your pin number:'))
        while len(pinno) != 4 or (pinno.isalpha()) or (not pinno.isdigit()):
            print('Error !')
            print("Not a 4 digit pin number")
            pinno = str(input('Enter your Pin number:'))
        pinno = int(pinno)
        with open("record.json", "r", encoding="utf-8")as file:
            data = json.load(file)
            store_data = data.copy()
            for i in store_data:
                cheak_acc = i.get("account")
                cheak_pin = i.get("pin")
                if accountno == cheak_acc and pinno == cheak_pin:
                    print("Access")
                    account_no = i.get("account")
                    pin = i.get("pin")
                    first_name = i.get("first_name")
                    last_name = i.get("last_name")
                    phone = i.get("phone")
                    balance = i.get("balance")
                    person = Account(first_name, last_name, phone, account_no, pin, balance)
                    person.access_account()
                else:
                    continue


def menu():
    """MENU"""
    clear()
    print("Welcome to SS Bank")
    print("Please select 1 of the menu items:")
    print("1. Create Your Account")
    print("2. Access Your Account")
    print("3. Exit")
    while True:
        try:
            option = int(input("Enter your option : "))
            if option == 1:
                user_data()
                menu()
            elif option == 2:
                account_match()
            elif option == 3:
                break
            else:
                print("Invalid option!-----Enter [1 to 3]")
                continue
        except ValueError:
            print("Invalid option!-----Enter [1 to 3]")
            continue
    exit(0)


if __name__ == "__main__":
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    menu()
