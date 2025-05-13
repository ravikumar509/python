import sys
from colorama import Fore, Back, Style, init
from .Expense import Expense
from utils.FileOperations import FileOperations
from datetime import datetime
import json
class Tracker:
    menu_list = {"0":"Exit","1":"Income","2":"Expense","3":"Delete Expense","4":"Balance"}
    balance_value = 0
   

    def get_balance(self):
        Tracker.balance_value = FileOperations().get_balance()

    def show_bal_question(func):
        def wrapper(self):
            func(self)
            prompt = input(f"{Fore.YELLOW} do you want to show final balance?[y|yes]{Style.RESET_ALL}").lower()
            if(prompt == 'y' or prompt =='yes'):
                self.balance()
            else:
                self.menu()
        return wrapper

    def menu(self):
        try:
            print("\nkindly select the option from below list")
            for keys in Tracker.menu_list.keys():
                print(f"  {Fore.GREEN}{keys} : {Tracker.menu_list[keys]}{Style.RESET_ALL} ",end="\t")
            option = input(f"\n{Fore.YELLOW}\nselect either number option/type the option: {Style.RESET_ALL}").lower().strip()
            match option:
                case '0' | 'exit':
                    sys.exit(0)
                case '1' | 'income':
                     self.income()
                case '2' | 'expense':
                    self.expense()
                case '3' | 'delete' | 'delete expense':
                    self.delete()
                case '4' | 'balance':
                    self.balance() 
                case _:
                    print(f"{Fore.RED} Selected Wrong Option {Style.RESET_ALL}")
                    self.menu()
        except Exception as e:
            print(f"--something went wrong:{e}")
        else:
            self.menu()

    @show_bal_question
    def income(self):
        try:
            print(f"{Fore.YELLOW}\nKindly enter details your income transaction:{Style.RESET_ALL}")
            amount = float(input((f"{Fore.YELLOW}Enter Amount:{Style.RESET_ALL}")))
            if(amount<0):
                print(f"{Fore.RED}income cannot be NEGATIVE, Re-enter the details {Style.RESET_ALL}")
                self.income()
            category_value = self.income_category()
            expense = Expense("income",amount,category_value,datetime.now().strftime("%Y-%m-%d"))
            appended = FileOperations().append_transaction(expense.to_dict())
            if(appended == True):
                Tracker.balance_value += amount
                FileOperations().update_balance(Tracker.balance_value)
                print("Transaction updated succesfully")                
        except Exception as e:
            print(f"error from income module:{e}")
    
        

    @show_bal_question
    def expense(self):
        try:
            print(f"{Fore.YELLOW}\nKindly enter details your Expense transaction:{Style.RESET_ALL}")
            amount = float(input((f"{Fore.YELLOW}Enter Amount:{Style.RESET_ALL}")))
            if(amount<0):
                print(f"{Fore.RED}Expense cannot be NEGATIVE, Re-enter the details {Style.RESET_ALL}")
                self.expense()
            category_value = input("Enter expense category:")
            expense = Expense("expense",amount,category_value,datetime.now().strftime("%Y-%m-%d"))
            appended = FileOperations().append_transaction(expense.to_dict())
            if(appended == True):
                Tracker.balance_value -= amount
                FileOperations().update_balance(Tracker.balance_value)
                print("Transaction updated succesfully")
        except Exception as e:
            print(f"error from expense module:{e}")
    

    @show_bal_question
    def delete(self): 
        print(f"{Fore.GREEN} 0 : income\n 1 : expense {Style.RESET_ALL}")
        transaction_type = input(f"{Fore.YELLOW}select either number option/type the option:{Style.RESET_ALL}").lower()
        match transaction_type:
            case '0' | 'income':
                 amount_ = FileOperations().remove_transaction("income")
            case '1' | 'expense':
                 amount_ = FileOperations().remove_transaction("expense")
        Tracker.balance_value+= amount_
        FileOperations().update_balance(Tracker.balance_value)

        
    def balance(self):
        print(f"->->-> Curret balance:{Fore.GREEN if Tracker.balance_value > 0 else Fore.RED }{Tracker.balance_value}{Style.RESET_ALL} <-<-<-")
        self.menu()
    
    def income_category(self):
        income_category_details = {"0":"Exit","1":"Salary","2":"Free Lancing","3":"Business"}
        for keys in income_category_details.keys():
            print(f"{Fore.GREEN}{keys} : {income_category_details[keys]}{Style.RESET_ALL}", end="\t")
        category_value = input(f"{Fore.YELLOW}\nselect either number option/type the option:{Style.RESET_ALL}").lower()
        match category_value:
            case '0' | 'q':
                sys.exit(0)
            case '1' | 'salary':
                return 'SALARY'
            case '2' | 'free' | 'free lancing':
                return 'FREE LANCING'
            case '3' | 'business':
                return "BUSINESS"
            case _:
                income_category =input(f"{Fore.RED} please select proper input{Style.RESET_ALL}")                
                return income_category()







        
