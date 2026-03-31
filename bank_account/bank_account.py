
from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    LOW_BALANCE_LEVEL = 500.0
    LARGE_TRANSACTION_THRESHOLD = 10000.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        super().__init__()  # Initialize Subject's observer list
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number should be integer.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number should be integer.")
        
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0
        
        if isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()
    
    @property
    def account_number(self) -> int:
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def balance(self):
        return self.__balance

    
    def update_balance(self, amount: float):
        
        try:
            self.__balance += float(amount)
        except Exception:
            pass


    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.update_balance(amount)

    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Cannot withdraw more than balance.")
        self.update_balance(-amount)

    @property
    def date_created(self) -> date:
        return self.__date_created 
    
    @abstractmethod
    def get_service_charges(self) -> float:
        pass
    
    def __str__(self):
        return (f"/nAccount number: {self.__account_number}"
                f"Balance: ${self.__balance:,.2f}"
                f"Date created : {self.__date_created}")