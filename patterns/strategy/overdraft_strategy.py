from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):

    def __init__(self, overdraft_limit, overdraft_rate):
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account):

        # if balance is above or equal to overdraft
        if account.balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE

        # calculate overdraft fee
        overdraft_fee = (self._overdraft_limit - account.balance) * self._overdraft_rate

        return self.BASE_SERVICE_CHARGE + overdraft_fee