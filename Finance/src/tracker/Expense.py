from datetime import datetime

class Expense:
    """
    A class to represent a financial transaction (either income or expense).
    Stores transaction details and provides property-based access and conversion to dictionary.
    """

    def __init__(self, expense_type, amount, category, date):
        """
        Initializes the Expense object with required details.
        Generates a unique ID based on the timestamp.
        """
        self.__id = datetime.now().strftime("%Y%m%d%H%M%S%f")  # Unique ID using timestamp
        self.__expense_type = expense_type  # Type: 'income' or 'expense'
        self.__amount = amount  # Monetary value of the transaction
        self.__category = category  # Category of the transaction
        self.__date = date  # Date of the transaction (string format)

    # ---------------- Properties (Getter/Setter methods) ----------------

    @property
    def id(self):
        """Returns the unique ID of the transaction."""
        return self.__id

    @property
    def expense_type(self):
        """Returns the type of transaction (income/expense)."""
        return self.__expense_type

    @expense_type.setter
    def expense_type(self, value):
        """Sets the transaction type."""
        self.__expense_type = value

    @property
    def category(self):
        """Returns the category of the transaction."""
        return self.__category

    @category.setter
    def category(self, value):
        """Sets the transaction category."""
        self.__category = value

    @property
    def amount(self):
        """Returns the amount of the transaction."""
        return self.__amount

    @amount.setter
    def amount(self, value):
        """Sets the amount of the transaction."""
        self.__amount = value

    @property
    def date(self):
        """Returns the date of the transaction."""
        return self.__date

    @date.setter
    def date(self, value):
        """Sets the date of the transaction."""
        self.__date = value  # ✅ Fixed: 'date' was undefined in your original getter

    # ---------------- Dunder Methods ----------------

    def __repr__(self):
        """
        Returns a developer-friendly string representation of the Expense object.
        Useful for debugging.
        """
        return (f"Expense(expense_type='{self.__expense_type}', amount={self.__amount}, "
                f"category='{self.__category}', date='{self.__date}')")

    def __str__(self):
        """
        Returns a user-friendly string version of the object (e.g., for printing).
        """
        return (f"{{'expense_type': '{self.__expense_type}', 'amount': {self.__amount}, "
                f"'category': '{self.__category}', 'date': '{self.__date}'}}")

    # ---------------- Utility Methods ----------------

    def to_dict(self):
        """
        Converts the Expense object into a dictionary format suitable for JSON serialization.
        """
        return {
            "id": self.__id,
            "expense_type": self.__expense_type,
            "amount": self.__amount,
            "category": self.__category,
            "date": self.__date
        }
