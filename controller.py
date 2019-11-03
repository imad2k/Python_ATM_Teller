from model import Account, authentication
import viewer

def run():
    while True:
        choice = viewer.run_menu()
        #Create new account
        if choice == "1":
            name = viewer.get_name()
            pin = viewer.get_pin()
            new_acct = Account(name, pin)
            new_acct.create_acct()
        #Exiting customer Menu
        elif choice == "2":
            viewer.customer_menu()
            # viewer.existing_customer_menu()
            return
        elif choice == "3":
            viewer.goodbye()
            return
        else:
            viewer.bad_input()

#account = Account.login(user,pass)
# def customer_menu(new_acct):


def customer_menu():
    while True:
        
        name = viewer.get_name()
        pin = viewer.get_pin()
        choice = viewer.existing_customer_menu()
        # pin = viewer.get_pin()
        # auth = authentication(name, pin)
        # if auth:
        #     #load method that will load account with name and pin for auth
        #     # current_acct = name.load_acct()
        #     name = name()
        #     choice = viewer.existing_customer_menu()
        # else:
        #     viewer.wrong_pin()
                
        
        
        #Deposit
        if choice == "1":
            acct = name.load_acct()
            amount = viewer.get_deposit_input()
            # new_acct.deposit(name, amount)
            acct.deposit(amount)
                
        #Get Balance    
        elif choice == "2":
            
            balance = Account.get_balance(name)
            name.show_balance(balance)
            

        #Withdraw   
        elif choice == "3":
            withdraw_amount = viewer.get_withdraw_input()
            name.withdraw(name, withdraw_amount)
            
         #Update Pin   
        elif choice == "4":
            
            new_pin = viewer.change_pin()
            name.update_pin(name, new_pin)
            
        elif choice == "5":
            viewer.goodbye()
        else:
            viewer.bad_input()

            


if __name__ == "__main__":
    
    run()
    
    
            
            
            
        
        
       