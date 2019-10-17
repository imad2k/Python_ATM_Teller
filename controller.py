import model
import viewer

def run():
    while True:
        choice = viewer.run_menu()
        #Create new account
        if choice == "1":
            name = viewer.get_name()
            pin = viewer.get_pin()
            new_acct_num = viewer.create_account_num()
            
            model.create_acct(name, pin, new_acct_num)
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
        choice = viewer.existing_customer_menu()
        #Deposit
        if choice == "1":
            #Authentication
            name = viewer.get_name()
            pin = viewer.get_pin()
            auth_validation = model.authentication(name, pin)
            if auth_validation == True:
                deposit = viewer.get_deposit_input()
                model.deposit(name, deposit)
            else:
                viewer.wrong_pin()
                
        #Get Balance    
        elif choice == "2":
            #Authentication
            name = viewer.get_name()
            pin = viewer.get_pin()
            print(name, pin)
            auth_validation = model.authentication(name, pin)
            print(auth_validation)
            if auth_validation == True:
                balance = model.get_balance(name)
                viewer.show_balance(balance)
            else:
                viewer.wrong_pin()
        #Withdraw   
        elif choice == "3":
            #Authentication
            name = viewer.get_name()
            pin = viewer.get_pin()
            auth_validation = model.authentication(name, pin)
            if auth_validation == True:
                #Withdraw    
                withdraw_amount = viewer.get_withdraw_input()
                model.withdraw(name, withdraw_amount)
            else:
                viewer.wrong_pin()
         #Update Pin   
        elif choice == "4":
            #Authentication
            name = viewer.get_name()
            pin = viewer.get_pin()
            auth_validation = model.authentication(name, pin)
            if auth_validation == True:
                #Update Pin
                new_pin = viewer.change_pin()
                model.update_pin(name, new_pin)
            else:
                viewer.wrong_pin()
            
        elif choice == "5":
            viewer.goodbye()
        else:
            viewer.bad_input()

            


if __name__ == "__main__":
    
    run()
    
    
            
            
            
        
        
       