"""Defines the AccountDetailsWindow class."""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

class AccountDetailsWindow(DetailsWindow):
    """Represents a detail window used to display account details and 
    perform bank account transactions.
    """

    def __init__(self, account: BankAccount) -> None:
        """Initializes a new instance of the AccountDetailsWindow class.
        
        Args:
            account (BankAccount): The bank account to be displayed.
        """

        super().__init__()
