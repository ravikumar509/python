import json
import os
from colorama import Fore, Style  # Used for color formatting in CLI output

class FileOperations:
    """
    Handles file read/write operations for transaction data and balance tracking.
    """
    # File paths for storing transactions and balance data
    file_path = os.path.join("data", "expenses.json")
    balance_file = os.path.join("data", "balance.json")

    def append_transaction(self, transaction):
        """
        Appends a new transaction (income/expense) to the expenses.json file.

        Args:
            transaction (dict): A dictionary containing transaction details.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with open(FileOperations.file_path, "r") as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, list):
                        data = []  # Reset if invalid format
                except json.JSONDecodeError as e:
                    print(f"JSON decoding error: {e}")
                    data = []

            data.append(transaction)  # Append new transaction

            with open(FileOperations.file_path, "w") as f:
                json.dump(data, f, indent=4)  # Save updated data
            return True

        except Exception as e:
            print("Transaction failed.")
            return False

    def remove_transaction(self, transaction_type):
        """
        Allows the user to remove a transaction (income/expense) by selecting from a list.

        Args:
            transaction_type (str): Type of transaction to delete ("income" or "expense").

        Returns:
            float: The amount associated with the removed transaction (used to update balance).
        """
        try:
            transaction_list = []
            updated_data = []
            transaction_amount = 0

            with open(FileOperations.file_path, 'r') as f:
                data = json.load(f)

                if not isinstance(data, list):
                    return []

                count = 0
                for i, transaction in enumerate(data):
                    if transaction['expense_type'] == transaction_type:
                        transaction_list.append(transaction['id'])
                        print("***********************************************************")
                        print(f"{Fore.YELLOW}Enter{Style.RESET_ALL} \"{Fore.RED}{count}{Style.RESET_ALL}\" {Fore.YELLOW}to delete this transaction:{Style.RESET_ALL}")
                        count += 1
                        print(f"{transaction['expense_type']}, {transaction['amount']}, {transaction['category']}, {transaction['date']}")

                if count > 0:
                    print("***********************************************************")
                    index = int(input(f"\nEnter the transaction number to delete: "))
                    if len(transaction_list) <= index:
                        print(f"{Fore.RED}Entered wrong index{Style.RESET_ALL}")
                        return 0

                    # Process deletion
                    for record in data:
                        if record['id'] == transaction_list[index]:
                            if transaction_type == "expense":
                                transaction_amount += record['amount']
                            else:
                                transaction_amount -= record['amount']
                        else:
                            updated_data.append(record)

                    with open(FileOperations.file_path, "w") as f:
                        json.dump(updated_data, f, indent=4)
                        print("->->-> Transaction removed <-<-<-")

                    return transaction_amount

                else:
                    print(f"{Fore.RED}No Transactions available{Style.RESET_ALL}")
                    return 0

        except Exception as e:
            print(f"Error while reading transactions: {e}")

    def get_balance(self):
        """
        Reads and returns the current balance from balance.json.

        Returns:
            float: The current balance.
        """
        with open(FileOperations.balance_file, 'r') as f:
            data = json.load(f)
            return data['balance']

    def update_balance(self, amount):
        """
        Updates the current balance in balance.json.

        Args:
            amount (float): The new balance value to store.
        """
        with open(FileOperations.balance_file, "w") as f:
            json.dump({"balance": amount}, f, indent=4)
