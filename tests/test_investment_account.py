import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def test_init_valid_attributes(self):
        account = InvestmentAccount(
            account_number=2004,
            client_number=622,
            balance=500.00,
            date_created=date(2026, 2, 13),
            management_fee=1.99
        )

        self.assertEqual(account.account_number, 2004)
        self.assertEqual(account.client_number, 622)
        self.assertEqual(round(account.balance, 2), 500.00)
        self.assertEqual(account.date_created, date(2026, 2, 13))
        self.assertEqual(account._InvestmentAccount__management_fee
, 1.99)

    def test_init_invalid_management_fee(self):
        account = InvestmentAccount(2004, 622, 500.00, date.today(), management_fee="invalid")
        self.assertEqual(account._InvestmentAccount__management_fee
, 2.55)

    def test_get_service_charges_created_more_than_10_years(self):
        old_date = date.today() - timedelta(days=365*11)
        account = InvestmentAccount(2004, 622, 500.00, old_date, management_fee=2.55)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_get_service_charges_account_exactly_10_years(self):
        ten_years_ago = date.today() - timedelta(days=int(10*365.25))
        account = InvestmentAccount(2004, 622, 500.00, ten_years_ago, management_fee=2.55)
        expected = 0.50 + account._InvestmentAccount__management_fee

        self.assertEqual(round(account.get_service_charges(), 2), round(expected, 2))
        
    def test_get_service_charges_date_within_10_years(self):
        recent_date = date.today() - timedelta(days=365*5)
        account = InvestmentAccount(2004, 622, 500.00, recent_date, management_fee=2.55)
        expected = 0.50 + account._InvestmentAccount__management_fee

        self.assertEqual(round(account.get_service_charges(), 2), round(expected, 2))

    def test_str_waived_management_fee(self):
        old_date = date.today() - timedelta(days=365*11)
        account = InvestmentAccount(2004, 622, 500.00, old_date, management_fee=2.55)
        expected_str = (
            f"Account Number: 2004 Balance: $500.00\n"
            f"Date Created: {account.date_created} Management Fee: Waived Account Type: Investment"
        )
        self.assertEqual(str(account), expected_str)

    def test_str_management_fee(self):
        recent_date = date.today() - timedelta(days=365*5)
        account = InvestmentAccount(2004, 622, 500.00, recent_date, management_fee=2.55)
        expected_str = (
            f"Account Number: 2004 Balance: $500.00\n"
            f"Date Created: {account.date_created} Management Fee: ${account._InvestmentAccount__management_fee:.2f} Account Type: Investment"
        )
        self.assertEqual(str(account), expected_str)

if __name__ == "__main__":
    unittest.main()
    