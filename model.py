import os
import json
import random

PATH = os.path.dirname(__file__)
DATA = "accounts.json"
DATAPATH = os.path.join(PATH, DATA)

def load_data():
    with open(DATAPATH, "r") as file_object:
        dictionary = json.load(file_object)
    return dictionary

def save(data_dict):
    with open(DATAPATH, 'w') as file_object:
        json.dump(data_dict, file_object, indent=2)
 
def create_acct(customer_name, customer_pin, customer_acct_num):
    data = load_data()
    # print(customer_name, customer_pin)
    # zero_balance = [0]
    data[customer_name] = {"balance":[0], "pin":customer_pin, "acct_num":customer_acct_num}
    
    save(data)
        
def authentication(customer_name, pin):
    data = load_data()
    customer_pin = data[customer_name]["pin"]
    print(customer_pin == pin)
    if pin == customer_pin:
        return True
    else:
        return False 


def deposit(customer_name, amount):
    data = load_data()
    balance = data[customer_name]["balance"]
    new_balance = balance.pop() + int(amount)
    
    # data[customer_name]["balance"] + new_balance
    # new_balance = data[customer_name]["balance"]+ int(amount)
    data[customer_name]["balance"].append(int(new_balance))
    save(data)

def withdraw(customer_name, amount):
    data = load_data()
    balance = data[customer_name]["balance"].pop()
    new_balance = balance - int(amount)
    # new_balance = data[customer_name]["balance"].pop() - int(amount)
    # data["acct_num"]["balance"].pop()
    data[customer_name]["balance"].append(int(new_balance))
    save(data)
    
def get_balance(customer_name):
    data = load_data()[customer_name]
    acct_balance = data["balance"][:-1]
    
    return acct_balance
    
def update_pin(customer_name, new_pin):
    data = load_data()
    # customer_name = customer_name
    updated_pin = new_pin
    data[customer_name]["pin"].clear()
    data[customer_name]["pin"].append(int(updated_pin))
    
# def transfer(customer_name, customer_name):
    





