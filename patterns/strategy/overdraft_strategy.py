from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):

    def __init__(self, overdraft_limit, overdraft_fee):
        self._overdraft_limit = overdraft_limit
        self._overdraft_fee = overdraft_fee

    def calculate_service_charges(self, account):

        if account.balance < self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE + self._overdraft_fee

        return self.BASE_SERVICE_CHARGE