"""Unit testing for the BankAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from datetime import date
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(40355, 2050, 6000.00, date.today())
    
    def test_init_valid_attributes_set(self):
        # Act
        bank_account = BankAccount(40355, 2050, 6000.00, date.today())

        # Assert
        self.assertEqual(40355, bank_account._BankAccount__account_number)
        self.assertEqual(2050, bank_account._BankAccount__client_number)
        self.assertEqual(round(6000.00, 2), round(bank_account._BankAccount__balance, 2))

    def test_init_non_numeric_balance_sets_zero(self):
        # Act
        bank_account = BankAccount(40355, 2050, "sun", date.today())

        # Assert
        self.assertEqual(0.0, bank_account._BankAccount__balance)

    def test_init_non_numeric_account_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            BankAccount("xyz", 2050, 6000.00, date.today())
    
    def test_init_non_numeric_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            BankAccount(40355, "abc", 6000.00, date.today())

    def test_account_number_getter(self):
        self.assertEqual(self.bank_account.account_number, 40355)

    def test_client_number_getter(self):
        self.assertEqual(self.bank_account.client_number, 2050)

    def test_balance_getter(self):
        self.assertEqual(self.bank_account.balance, 6000.00)

    def test_update_balance_positive_amount(self):
        self.bank_account.update_balance(500.00)
        self.assertEqual(self.bank_account.balance, 6500.00)

    def test_update_balance_negative_amount(self):
        self.bank_account.update_balance(-400.00)
        self.assertEqual(self.bank_account.balance, 5600.00)

    def test_update_balance_non_numeric_amount(self):
        initial_balance = self.bank_account.balance
        self.bank_account.update_balance("abc")
        self.assertEqual(self.bank_account.balance, initial_balance)

    def test_deposit_valid_amount(self):
        self.bank_account.deposit(600.00)
        self.assertEqual(self.bank_account.balance, 6600.00)

    def test_deposit_negative_amount_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-300.00)

    def test_withdraw_valid_amount(self):
        self.bank_account.withdraw(800.00)
        self.assertEqual(self.bank_account.balance, 5200.00)

    def test_withdraw_negative_amount_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-100.00)

    def test_withdraw_exceed_balance_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(7000.00)

    def test_str_returns_expected_format(self):
        expected = "Account Number: 40355 Balance: $6000.00\n"
        self.assertEqual(str(self.bank_account), expected)


if __name__ == "__main__":
    unittest.main()
