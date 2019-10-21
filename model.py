import os
import json
import random
# import viewer 

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


class Account:
    
    #took out customer_acct_num
    def __init__(self, customer_name, customer_pin):
        self.customer_name = customer_name
        self.customer_pin = customer_pin
        self.customer_acct_num = random.randint(500, 1000000)
    
    
    #took out customer_name, customer_pin, customer_acct_num    
    def create_acct(self):
        data = load_data()
        data[self.customer_name] = {"balance":[0], "pin":[self.customer_pin], "acct_num":self.customer_acct_num}
        save(data)    
  
    #took out customer_name
    def deposit(self, name, amount):
        data = load_data()
        balance = data[name]["balance"]
        new_balance = balance.pop() + int(amount)
        data[self.customer_name]["balance"].append(int(new_balance))
        save(data)
 
    
    #took out customer_name
    def withdraw(self, amount):
        data = load_data()
        balance = data[self.customer_name]["balance"].pop()
        new_balance = balance - int(amount)
        data[self.customer_name]["balance"].append(int(new_balance))
        save(data)
        
    
    #took out customer_name
    def get_balance(self):
        data = load_data()
        acct_balance = data[self.customer_name]["balance"].pop()
        # acct_balance = data["balance"][:-1]
        return acct_balance

    
    #took out customer_name
    def update_pin(self, new_pin):
        data = load_data()
        data[self.customer_name]["pin"].clear()
        data[self.customer_name]["pin"].append(int(new_pin))
        save(data)


    # def transfer(customer_name, customer_name):
    

#took out customer_name
def authentication(name, pin):
    data = load_data()
    customer_name = data[name]
    customer_pin = data[name]["pin"].pop()
        # print(self.customer_pin == pin)
    if name == customer_name and pin == customer_pin:
        return True
    # else:
    #     viewer.wrong_pin()
    

    
    # def create_account_num():
    # acct_num = random.randint(500, 1000000)
    # return acct_num

    





