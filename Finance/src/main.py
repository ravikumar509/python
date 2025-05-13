# Entry point for the Expense Tracker application

from tracker.Tracker import Tracker  # Importing the main Tracker class that handles operations

def main():
    """
    Main function to initiate the expense tracker application.
    It displays a welcome message, fetches the current balance, and launches the menu.
    """
    print("***************************")
    print("Welcome to Expenses Tracker")
    print("***************************")

    # Create an instance of the Tracker class
    tracker = Tracker()

    # Initialize the balance (read from file)
    tracker.get_balance()

    # Start the interactive menu for user operations
    tracker.menu()

# Ensures that main() is executed only when this script is run directly
if __name__ == "__main__":
    main()
