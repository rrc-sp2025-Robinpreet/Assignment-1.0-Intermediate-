__author__ = "Robinpreet Kaur"
__version__ = "2.49.0.windows.1"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self._overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self._overdraft_limit = -100.0

        try:
            self._overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self._overdraft_rate = 0.05

        # Strategy Pattern
        self.__service_charge_strategy = OverdraftStrategy(
            self._overdraft_limit,
            self._overdraft_rate
        )

    def get_service_charges(self):
        return self.__service_charge_strategy.calculate_service_charges(self)

    def __str__(self):

        base_str = super().__str__()
        overdraft_limit_str = f"${self._overdraft_limit:,.2f}"
        overdraft_rate_str = f"{self._overdraft_rate * 100:.2f}%"

        return (
            f"{base_str.strip()}\n"
            f"Overdraft Limit: {overdraft_limit_str} "
            f"Overdraft Rate: {overdraft_rate_str} "
            f"Account Type: Chequing"
        )