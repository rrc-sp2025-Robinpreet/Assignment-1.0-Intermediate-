import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

# Run with:
# python -m unittest tests.test_savings_account


class TestSavingsAccount(unittest.TestCase):

    def test_init_valid_attributes(self):
        account = SavingsAccount(2003, 412, 700.00, date(2024, 10, 3), 500.00)

        self.assertEqual(2003, account.account_number)
        self.assertEqual(412, account.client_number)
        self.assertEqual(700.0, account.balance)
        self.assertEqual(date(2024, 10, 3), account.date_created)
        self.assertEqual(500.0, account._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance(self):
        account = SavingsAccount(2003, 412, 700.00, date(2024, 10, 3), "five hundred")
        self.assertEqual(50.0, account._SavingsAccount__minimum_balance)

    def test_get_service_charges_balance_greater(self):
        account = SavingsAccount(2003, 412, 1000.00, date(2024, 10, 3), 500.00)
        expected = 0.50
        actual = account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    def test_get_service_charges_balance_equal(self):
        account = SavingsAccount(2003, 412, 500.00, date(2024, 10, 3), 500.00)
        expected = 0.50
        actual = account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    def test_get_service_charges_balance_less(self):
        account = SavingsAccount(2003, 412, 400.00, date(2024, 10, 3), 500.00)
        expected = 1.00
        actual = account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    def test_str_method(self):
        account = SavingsAccount(2003, 412, 700.0, date(2024, 10, 3), 500.00)

        expected_str = (
            "Account Number: 2003 Balance: $700.00\n"
            "Date Created: 2024-10-03Minimum Balance: $500.00 Account Type: Savings"
        )

        self.assertEqual(str(account), expected_str)


if __name__ == "__main__":
    unittest.main()