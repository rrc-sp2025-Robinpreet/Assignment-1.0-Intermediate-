__author__ = "Robinpreet Kaur"
__version__ = "2.49.0.windows.1"



from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    ChequingAccount class extends BankAccount for clients with frequent transactions.
    """

    def __init__(self, account_number:int, client_number:int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initialize CheckingAccount with overdraft attributes.
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self._overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self._overdraft_limit = -100.0

        try:
            self._overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self._overdraft_rate = 0.05
    
    def __str__(self):
        """
        Return string representation with balance, overdraft, rate, and account type.
        """

        base_str = super().__str__()
        overdraft_limit_str = f"${self._overdraft_limit:,.2f}"
        overdraft_rate_str = f"{self._overdraft_rate * 100:.2f}%"
        return (
            f"{base_str.strip()}\n"
            f"Overdraft Limit: {overdraft_limit_str} "
            f"Overdraft Rate: {overdraft_rate_str} "
            f"Account Type: Chequing"
        )
    
    def get_service_charges(self) -> float:
        """
        Calculate service charges based on balance and overdraft.
        """

        if self.balance >= self._overdraft_limit:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            overdraft_fee = (self._overdraft_limit - self.balance) * self._overdraft_rate
            return round(BankAccount.BASE_SERVICE_CHARGE + overdraft_fee, 2)
        