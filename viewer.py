import random

def run_menu():
    print()
    print("Welcome to Bank of Abusam")
    print()
    print("How many I help you today?")
    print("1. Create a new account")
    print("2. Log into your account")
    print("3. Exit Screen")
    return input()

def existing_customer_menu():
    print()
    print("Welcome Back")
    print()
    print("What would you like to do today?")
    print("1. Deposit Funds")
    print("2. Check My Balance")
    print("3. Withdraw From My Account")
    print("4. Change My Pin")
    print("5. Exit Screen")
    return input()

def bad_input():
    print()
    print("Sorry that is an invalid option, please try again")
    
def goodbye():
    print()
    print("Goodbye, have a great day!")
    


def get_deposit_input():
    print()
    print("How much would you like to deposit today? ")
    return input(int())

def get_withdraw_input():
    print()
    print("How much would you like to get out today? ")
    return input(int())

def get_name():
    print()
    name = input("Please enter your name: ")
    return name

def get_pin():
    print()
    pin = input("Please enter your pin: ")
    return pin

def show_balance(balance):
    print()
    print("Your current balance is {}.".format(balance))

    
def success():
    print()
    print("You authenticated your identity!")


def create_account_num():
    # print()
    # print("Happy to hear you want to create an account with us. Please fill out the following form")
    # customer_name = input("Please enter your name: ")
    # customer_pin = input("Please enter a pin: ")
    acct_num = random.randint(500, 1000000)
    return acct_num

def change_pin():
    print()
    # customer_name = input("Please Enter Your Name")
    # pin = input("Please Enter Your Current Pin")
    new_pin = input("What would you like to change your pin to? ")
    return new_pin
