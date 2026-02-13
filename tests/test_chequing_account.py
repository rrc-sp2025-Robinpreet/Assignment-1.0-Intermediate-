import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.bank_account import BankAccount

class TestChequingAccount(unittest.TestCase):

    def test_init_valid_attributes_set(self):
        account = ChequingAccount(
            account_number=2004,
            client_number=622,
            balance=500.00,
            date_created=date(2026, 2, 13),
            overdraft_limit=-200.0,
            overdraft_rate=0.05
        )

        self.assertEqual(account.account_number, 2004)
        self.assertEqual(account.client_number, 622)
        self.assertEqual(account.balance, 500.00)
        self.assertEqual(account.date_created, date(2026, 2, 13))
        self.assertEqual(account._overdraft_limit, -200.0)
        self.assertEqual(account._overdraft_rate, 0.05)

    def test_init_invalid_overdraft_limit_returns_default_value(self):
        account = ChequingAccount(2004, 622, 500.00, date.today(), overdraft_limit="invalid", overdraft_rate=0.05)
        self.assertEqual(account._overdraft_limit, -100.0)

    def test_init_invalid_overdraft_rate_returns_default_value(self):
        account = ChequingAccount(2004, 622, 500.00, date.today(), -200.0, overdraft_rate="invalid")
        self.assertEqual(account._overdraft_rate, 0.05)

    def test_init_invalid_data_created_returns_set_value(self):
        account = ChequingAccount(2004, 622, 500.00, date_created="2026-2-13", overdraft_limit=-200.0, overdraft_rate=0.05)
        self.assertEqual(account.date_created, date.today())

    def test_get_service_charges_balance_above_overdraft(self):
        account = ChequingAccount(2004, 622, 0.00, date.today(), overdraft_limit=-100.0, overdraft_rate=0.05)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)
    
    def test_get_service_charges_balance_below_overdraft(self):
        account = ChequingAccount(2004, 622, -600.00, date.today(), overdraft_limit=-100.0, overdraft_rate=0.05)
        expected = 0.50 + (-100 - -600) * 0.05
        self.assertEqual(round(account.get_service_charges(), 2), round(expected, 2))

    def test_get_service_charges_balance_equal_overdraft(self):
        account = ChequingAccount(2004, 622, -100.00, date.today(), overdraft_limit=-100.0, overdraft_rate=0.05)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)
    
    def test_str_method(self):
        account = ChequingAccount(2004, 622, 500.00, date(2026, 2, 13), overdraft_limit=-200.0, overdraft_rate=0.05)
        expected_str = (
            "Account Number: 2004 Balance: $500.00\n"
            "Overdraft Limit: $-200.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )
        self.assertEqual(str(account), expected_str)

if __name__ == "__main__":
    unittest.main()