from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):

    SERVICE_CHARGE_PREMIUM = 5.00

    def __init__(self, minimum_balance):
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account):

        if account.balance < self._minimum_balance:
            return self.SERVICE_CHARGE_PREMIUM

        return self.BASE_SERVICE_CHARGE