import json
import os
from colorama import Fore, Back, Style, init

class FileOperations:
    file_path =os.path.join("data","expenses.json")
    balance_file = os.path.join("data","balance.json")

    def append_transaction(self,transaction):
        try:
            with open(FileOperations.file_path,"r") as f:
                try:
                    data = json.load(f)
                    if not isinstance(data,list):
                        data = []

                except json.JSONDecodeError as e:
                    print(f"json error:{e}")
                    data = []
                data.append(transaction)
                with open(FileOperations.file_path,"w") as f:
                    json.dump(data,f,indent=4)                
                return True
        except Exception as e:
            print(f"transaction failed")
            return False
        
    def remove_transaction(self,transaction_type):
        try:
            transaction_list = []
            updated_data =[]
            transaction_amount =0
            with open(FileOperations.file_path,'r') as f:
                data = json.load(f)
                if not isinstance(data,list):
                    return []
                else:
                    count =0
                    for i,transaction in enumerate(data):
                        if(transaction['expense_type'] == transaction_type):
                            transaction_list.append(transaction['id'])
                            print("***********************************************************")
                            print(f"{Fore.YELLOW}enter{Style.RESET_ALL} \"{Fore.RED}{count}{Style.RESET_ALL}\" {Fore.YELLOW}to delete this transaction:{Style.RESET_ALL}")
                            count+=1
                            print(f"{transaction['expense_type']}, {transaction['amount']}, {transaction['category']}, {transaction['date']}")
                if count > 0:
                    print("***********************************************************")
                    index = int(input(f"\nenter the transaction number to delete: "))
                    if len(transaction_list) <= index:
                        print(f"{Fore.RED}entered wrong index{Style.RESET_ALL}")
                        print("\n")
                        self.get_all_transactions(transaction_type)
                    else:
                        for record in data:
                            if record['id'] == transaction_list[index]:
                                if transaction_type == "expense":
                                    transaction_amount += record['amount']
                                else:
                                    transaction_amount -= record['amount']
                            else:
                                updated_data.append(record)
                    with open(FileOperations.file_path,"w") as f:
                        json.dump(updated_data,f,indent=4)
                        print("->->->transaction removed<-<-<-")

                    return transaction_amount
                else:
                    print(f"{Fore.RED} No Transactions available{Style.RESET_ALL}")
                    return 0
        
        except Exception as e:
            print(f"error from reading transactions{e}")   
    
    def get_balance(self):
          with open(FileOperations.balance_file,'r') as f:
                data = json.load(f)
                return data['balance']
    
    def update_balance(self,amount):
        with open(FileOperations.balance_file,"w") as f:
                    json.dump({"balance":amount},f,indent=4) 
        