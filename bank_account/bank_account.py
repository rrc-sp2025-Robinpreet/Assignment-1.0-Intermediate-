
from abc import ABC
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
        self.__balance = float(balance)
        self._date_created = date_created if isinstance(date_created, date) else date.today()
        self._service_charge_strategy = None

    @property
    def balance(self):
        return self.__balance

    def update_balance(self, amount: float):
        self.__balance += amount
        self._check_notifications(amount)

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

    def _check_notifications(self, transaction_amount: float):
        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:.2f}: on account {self.__account_number}")
        if abs(transaction_amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${abs(transaction_amount):.2f}: on account {self.__account_number}")