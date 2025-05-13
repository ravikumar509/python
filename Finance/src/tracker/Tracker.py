import sys
from colorama import Fore, Back, Style, init
from .Expense import Expense
from utils.FileOperations import FileOperations
from datetime import datetime
import json
class Tracker:
    menu_list = {"0":"Exit","1":"Income","2":"Expense","3":"Delete Expense","4":"Show All Transactions","5":"balance"}
    balance_value = 0
   

    def get_balance(self):
        """
        Fetches the current balance from the data source and stores it as a class-level variable.
        
        This method retrieves the balance value from the external data source (such as a JSON file)
        using the FileOperations class. The fetched balance is then stored in the `Tracker.balance_value`
        attribute to allow easy access and tracking throughout the application's lifecycle.
        
        It is useful for initializing or updating the balance when needed.
        """
        Tracker.balance_value = FileOperations().get_balance()

    def show_bal_question(func):
        """
        A decorator function to wrap another function and ask the user if they want to 
        see the final balance after executing the wrapped function.
        
        Args:
            func (function): The function to be wrapped.

        Returns:
            function: The wrapper function that adds additional behavior.
        """
        
        def wrapper(self):
            """
              The wrapper function that calls the original function and asks the user
            whether to display the final balance or return to the main menu.

            Args:
                self: The instance of the class that contains the original function.
            """
            
            # Execute the original function
            func(self)
            
            # Ask the user if they want to see the final balance
            prompt = input(f"{Fore.YELLOW} do you want to show final balance?[y|yes]{Style.RESET_ALL}").lower()
            if(prompt == 'y' or prompt =='yes'):
                self.balance()
            else:
                self.menu()
        return wrapper

    def menu(self):
        """
        Displays the main menu and handles user input for different tracking actions.

        This method presents a list of available options (like income, expense, delete, balance, exit),
        takes the user's choice as input, and executes the corresponding method.

        It supports both numeric and textual input (e.g., '1' or 'income').
        Invalid inputs are handled gracefully with a message and the menu is shown again.

        Exceptions during execution are caught and displayed, and the menu is reloaded.
        """
        try:
            # Display menu options
            print("\nkindly select the option from below list")
            for keys in Tracker.menu_list.keys():
                print(f"  {Fore.GREEN}{keys} : {Tracker.menu_list[keys]}{Style.RESET_ALL} ",end="\t")
            option = input(f"\n{Fore.YELLOW}\nselect either number option/type the option: {Style.RESET_ALL}").lower().strip()
            
            # Handle user input using pattern matching (Python 3.10+)
            match option:
                case '0' | 'exit':
                    sys.exit(0)
                case '1' | 'income':
                     self.income()
                case '2' | 'expense':
                    self.expense()
                case '3' | 'delete' | 'delete expense':
                    self.delete()
                case '4' | 'show' | 'show all transactions':
                    self.show_all_transactions()
                case '5' | 'balance':
                    self.balance() 
                case _:
                    print(f"{Fore.RED} Selected Wrong Option {Style.RESET_ALL}")
                    self.menu()
        except Exception as e:
            # Catch and display any unexpected errors
            print(f"--something went wrong:{e}")
        else:
            # Continue showing the menu in a loop unless exited
            self.menu()

    @show_bal_question
    def income(self):
        """
        Handles the process of recording an income transaction.

        Steps:
        1. Prompts the user for income amount and category.
        2. Validates the input (amount must be non-negative).
        3. Creates an Expense object with type 'income'.
        4. Appends the transaction to the expense JSON file.
        5. Updates the current balance in memory and saves it.
        6. Decorated with @show_bal_question to optionally show the balance after transaction.

        Exceptions during input or file operations are caught and reported.
        """
        try:
            # Prompt the user to enter income transaction details
            print(f"{Fore.YELLOW}\nKindly enter details your income transaction:{Style.RESET_ALL}")

            # Take amount input and convert to float
            amount = float(input((f"{Fore.YELLOW}Enter Amount:{Style.RESET_ALL}")))
        
            # Validate that income amount is not negative        
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
        """
        Handles the process of recording an expense transaction.

        Steps:
        1. Prompts the user for the expense amount and category.
        2. Validates the amount to ensure it's not negative.
        3. Creates an Expense object with type 'expense'.
        4. Appends the transaction to the expense JSON file.
        5. Deducts the amount from the current balance and updates it in the file.
        6. Decorated with @show_bal_question to optionally display the balance after entry.

        Exceptions during input or file operations are caught and reported.
        """
        try:
            # Prompt user to enter expense transaction details
            print(f"{Fore.YELLOW}\nKindly enter details your Expense transaction:{Style.RESET_ALL}")

            # Input and convert the amount
            amount = float(input((f"{Fore.YELLOW}Enter Amount:{Style.RESET_ALL}")))

            # Check for negative amount
            if(amount<0):
                print(f"{Fore.RED}Expense cannot be NEGATIVE, Re-enter the details {Style.RESET_ALL}")
                self.expense()
            category_value = input("Enter expense category:")
            expense = Expense("expense",amount,category_value,datetime.now().strftime("%Y-%m-%d"))
            
            # Save the transaction to the expenses JSON file
            appended = FileOperations().append_transaction(expense.to_dict())
            if(appended == True):
                # Deduct the expense from current balance and update file
                Tracker.balance_value -= amount
                FileOperations().update_balance(Tracker.balance_value)
                print("Transaction updated succesfully")
        except Exception as e:
            print(f"error from expense module:{e}")
    

    @show_bal_question
    def delete(self): 
        """
        
        Handles the deletion of a transaction (either income or expense).

        Steps:
        1. Prompts the user to choose the type of transaction to delete.
        2. Calls FileOperations to remove a transaction of the selected type.
        3. Adjusts the current balance based on the deleted amount.
        4. Updates the new balance in the data store.
        5. Decorated with @show_bal_question to optionally display the balance afterward.

        Note:
        - Assumes `remove_transaction` returns the amount that was deleted (positive number).
        - If income is deleted, balance is reduced. If expense is deleted, balance is increased.
        """
        
        # Show options to the user for type of transaction to delete
        print(f"{Fore.GREEN} 0 | q : quit \t1: income\t 2 : expense {Style.RESET_ALL}")
        transaction_type = input(f"{Fore.YELLOW}select either number option/type the option:{Style.RESET_ALL}").lower()
        match transaction_type:
            case '0' | 'q':
                sys.exit(0)
            case '1' | 'income':
                 amount_ = FileOperations().remove_transaction("income")
            case '2' | 'expense':
                 amount_ = FileOperations().remove_transaction("expense")            
            case _:
                self.delete()
        Tracker.balance_value+= amount_
        FileOperations().update_balance(Tracker.balance_value)

        
    def balance(self):
        """
         Displays the current balance to the user with color formatting:
        - Green if balance is positive
        - Red if balance is zero or negative

        After displaying the balance, it returns the user to the main menu.
        """
        print(f"->->-> Curret balance:{Fore.GREEN if Tracker.balance_value > 0 else Fore.RED }{Tracker.balance_value}{Style.RESET_ALL} <-<-<-")
        self.menu()
    
    def income_category(self):
        """
         Prompts the user to select an income category from a predefined list.

        Steps:
        1. Displays a menu of income category options.
        2. Accepts user input as number or text (case-insensitive).
        3. Maps input to the corresponding category and returns it.
        4. Exits the program if the user selects 0 or 'q'.
        5. If input is invalid, recursively prompts again until a valid choice is made.
        """
        income_category_details = {"0 | 'q'":"Exit","1":"Salary","2":"Free Lancing","3":"Business"}
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
            
    def show_all_transactions(self):
        """Fetches and displays all transactions from the expenses file"""
        try:
            with open(FileOperations.file_path, 'r') as f:
                data = json.load(f)
                if not isinstance(data, list) or len(data) == 0:
                    print(f"{Fore.RED}No transactions found.{Style.RESET_ALL}")
                    return
                
                print(f"{Fore.GREEN}--- All Transactions ---{Style.RESET_ALL}")
                for transaction in data:
                    print(f"ID: {transaction['id']}")
                    print(f"Type: {transaction['expense_type']}")
                    print(f"Amount: {transaction['amount']}")
                    print(f"Category: {transaction['category']}")
                    print(f"Date: {transaction['date']}")
                    print(f"{Fore.YELLOW}-----------------------------{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}Error reading transactions: {e}{Style.RESET_ALL}")







        
