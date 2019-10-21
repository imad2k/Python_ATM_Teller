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
            Account.create_acct(new_acct)
        #Exiting customer Menu
        elif choice == "2":
            customer_menu()
            return
        elif choice == "3":
            viewer.goodbye()
            return
        else:
            viewer.bad_input()


def customer_menu():
    while True:
        
        name = viewer.get_name()
        pin = viewer.get_pin()
        authentication(name, pin)
        choice = viewer.existing_customer_menu()
        
        #Deposit
        if choice == "1":
            
            amount = viewer.get_deposit_input()
            Account.deposit(name, amount)
                
        #Get Balance    
        elif choice == "2":
            
            balance = Account.get_balance(name)
            viewer.show_balance(balance)
            

        #Withdraw   
        elif choice == "3":
            withdraw_amount = viewer.get_withdraw_input()
            Account.withdraw(name, withdraw_amount)
            
         #Update Pin   
        elif choice == "4":
            
            new_pin = viewer.change_pin()
            Account.update_pin(name, new_pin)
            
        elif choice == "5":
            viewer.goodbye()
        else:
            viewer.bad_input()

            


if __name__ == "__main__":
    
    run()
    
    
            
            
            
        
        
       