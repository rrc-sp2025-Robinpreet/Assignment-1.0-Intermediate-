__author__ = "Robinpreet Kaur"
__version__ = "2.49.0.windows.1"


from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    Represents a short term saving plan.
    """


    def __init__(self, account_number: int, client_number:int, balance: float, date_created:date,
                 minimum_balance: float):
        """
        Initialize a SavingsAccount instance.

        Args:
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number representing the account holder.
            balance (float): The current balance of the bank account.
            date_created (date): The creation date of the account.
            minimum_balance (float): The minimum balance required to avoid premium service charges.

        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50.0

        # Strategy Pattern
        self.__service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def get_service_charges(self):
        """
        Calculate and service charge using MinimumBalanceStrategy.

        """
        return self.__service_charge_strategy.calculate_service_charges(self)

    def __str__(self):
        """
        Return a string representation of the SavingsAccount instance.

        Format:
            Account Number: {account_number} Balance: ${balance}
            Minimum Balance: ${minimum_balance} Account Type: Savings
        """
        base_str = super().__str__()  
        min_balance_str = f"${self.__minimum_balance:.2f}"

        return (
            f"{base_str.strip()}\n"
            f"Date Created: {self._date_created}"
            f"Minimum Balance: {min_balance_str} Account Type: Savings"
        )