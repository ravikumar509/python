from datetime import datetime
class Expense:
    def __init__(self,expense_type,amount,category,date):
        self.__id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.__expense_type = expense_type
        self.__amount = amount
        self.__category = category
        self.__date = date
    
    @property
    def id(self):
        return self.__id
    
    @property
    def expense_type(self):
        return self.__expense_type
    
    @expense_type.setter
    def expense_type(self,value):
        self.__expense_type = value
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self,value):
        self.__category = value
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self,value):
        self.__amount = value

    @property
    def date(self):
        self.__date = date
    
    @date.setter
    def date(self,value):
        self.__date =date

    def __repr__(self):
        return (f"Expense(expense_type='{self.__expense_type}',amount={self.__amount}),"
                f"category='{self.__category}, date={self.__date}")
    
    def __str__(self):
        return f"{{'expense_type': '{self.__expense_type}', 'amount': {self.__amount}, 'category': '{self.__category}', 'date': '{self.__date}'}}"

    def to_dict(self):
        return {
            "id" : self.__id,
            "expense_type" : self.__expense_type,
            "amount" : self.__amount,
            "category":self.__category,
            "date" : self.__date
        }

class Balance:
    def __init__(self,balance_value):
        self.__balance_value = balance_value
        
    @property
    def balance(self):
        return self.__balance_value
    
    @balance.setter
    def balance(self,value):
        self.__balance_value = value
    
    def to_dict(self):
        return {
            "balance" : self.__balance_value
        }