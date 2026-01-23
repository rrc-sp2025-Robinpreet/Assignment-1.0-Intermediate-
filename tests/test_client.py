"""Unit testing for the Client class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(2050, "Peter", "Parker", "peterparker@pixell.com")
        

    def test_init_valid_client_attributes_set(self):
        # Act
        client = Client(2050, "Peter", "Parker", "peterparker@pixell.com")

        # Assert
        self.assertEqual(2050, client._Client__client_number)
        self.assertEqual("Peter", client._Client__first_name)
        self.assertEqual("Parker", client._Client__last_name)
        self.assertEqual("peterparker@pixell.com", client._Client__email_address)
        
    def test_init_invalid_client_number_raised_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client("Thousand", "Peter", "Parker", "peterparker@pixell.com")

    def test_init_blank_first_name_raised_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client(2050, "", "Peter", "peterparker@pixell.com")

    def test_init_blank_last_name_raised_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client(2050, "Peter", "", "peterparker@pixell.com")

    def test_init_invalid_email(self):
        client = Client(2050, "Peter", "Parker", "invalid-email")
        self.assertEqual(client._Client__email_address, "email@pixell-river.com")

    def test_client_number_returns_valid_client_number(self):
        # Arrange
        expected = 2050

        # Act
        actual = self.client.client_number

        # Assert
        self.assertEqual(expected, actual)

    def test_first_name_returns_valid_first_name(self):
        # Arrange
        expected = "Peter"

        # Act
        actual = self.client.first_name

        # Assert
        self.assertEqual(expected, actual)

    def test_last_name_returns_valid_last_name(self):
        # Arrange 
        expected = "Parker"

        # Act
        actual = self.client.last_name

        # Assert
        self.assertEqual(expected, actual)

    def test_email_address_returns_valid_email_address(self):
        # Arrange
        expected = "peterparker@pixell.com"

        # Act
        actual = self.client.email_address

        # Assert
        self.assertEqual(expected, actual)

    def test_str_valid_client_formatted_string_returned(self):
        expected = "Parker, Peter [2050] - peterparker@pixell.com"
        
        self.assertEqual(expected, str(self.client))