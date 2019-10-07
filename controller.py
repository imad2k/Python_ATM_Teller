import model
import viewer

def run():
    while True:
        choice = viewer.run_menu()
        if choice == "1":
            name = viewer.get_name()
            pin = viewer.get_pin()
            new_acct_num = viewer.create_account_num()
            model.create_acct(name, pin, new_acct_num)
        elif choice == "2":
            viewer.existing_customer_menu()
            return
        elif choice == "3":
            viewer.goodbye()
            return
        else:
            viewer.bad_input()
            
def customer_menu():
    while True:
        choice = viewer.existing_customer_menu()
        if choice == "1":
            name = viewer.get_name()
            pin = viewer.get_pin()
            model.authentication(name, pin)
            # deposit = viewer.get_deposit_input()
            # model.deposit(name, deposit)
            viewer.success()
            return
            
        elif choice == "2":
            name = viewer.get_name()
            pin = viewer.get_pin()
            balance = model.get_balance(name)
            viewer.show_balance(balance)
            
        elif choice == "3":
            name = viewer.get_name()
            pin = viewer.get_pin()
            withdraw_amount = viewer.get_withdraw_input()
            model.withdraw(name, withdraw_amount)
            
        elif choice == "4":
            name = viewer.get_name()
            pin = viewer.get_pin()
            new_pin = viewer.change_pin()
            model.update_pin(name, new_pin)
        elif choice == "5":
            viewer.goodbye()
        else:
            viewer.bad_input()
            
if __name__ == "__main__":
    run()
    
            
            
            
            