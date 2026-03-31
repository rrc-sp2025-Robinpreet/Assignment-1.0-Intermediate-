from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.managementfee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):

    TEN_YEARS_AGO = date.today() - timedelta(days=int(10 * 365.25))

    def __init__(self, account_number, client_number,
                 balance, date_created, management_fee):

        super().__init__(account_number, client_number,
                         balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except (TypeError, ValueError):
            self.__management_fee = 2.55
        # Strategy Pattern
        self.__service_charge_strategy = ManagementFeeStrategy(self.__management_fee)
    @property
    def management_fee(self) -> float:
        return self.__management_fee

    def __str__(self):

        management_fee = "waived" if self.date_created <=self.TEN_YEARS_AGO else f"${self.__management_fee:,.2f}"

        return (
            super().__str__() +
            f"\nDate Created: {self.date_created} "
            f"Management Fee: {management_fee} "
            f"Account Type: Investment"
        )

    def get_service_charges(self):
        """
        Calculate service charges using ManagementFeeStrategy
        """
        return self.__service_charge_strategy.calculate_service_charges(self)
        