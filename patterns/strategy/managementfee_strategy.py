from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, management_fee):
        self._management_fee = management_fee

    def calculate_service_charges(self, account):

        if account.date_created > self.TEN_YEARS_AGO:
            return self._management_fee

        return 0