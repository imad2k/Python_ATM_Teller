import os
import json
import random

PATH = os.path.dirname(__file__)
DATA = "data.json"
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
    data[customer_name] = {"balance":[], "pin":[], "acct_num":[]}
    data[customer_name]["pin"].append(customer_pin)
    data[customer_name]["acct_num"].append(customer_acct_num)
    save(data)
        
def authentication(customer_name, pin):
    data = load_data()
    customer = data[customer_name]
    customer_pin = data[customer_name]["pin"]
    if customer_name == customer and pin == customer_pin:
        return True
    else:
        return False 


def deposit(customer_name, amount):
    data = load_data()
    new_balance = data[customer_name]["balance"] + int(amount)
    data[customer_name]["balance"].pop()
    data[customer_name]["balance"].append(int(new_balance))
    save(data)

def withdraw(customer_name, amount):
    data = load_data()
    new_balance = data[customer_name]["balance"] - int(amount)
    data["acct_num"]["balance"].pop()
    data["acct_num"]["balance"].append(int(new_balance))
    save(data)
    
def get_balance(customer_name):
    data = load_data()[customer_name]
    acct_balance = data["balance"]
    return acct_balance
    
def update_pin(customer_name, new_pin):
    data = load_data()
    updated_pin = new_pin
    data[customer_name]["pin"].pop()
    data[customer_name]["pin"].append(int(updated_pin))
    
# def transfer(customer_name, customer_name):
    





