"""Defines the AccountDetailsWindow class."""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Rbinpreet kaur"

class AccountDetailsWindow(DetailsWindow):
    """Represents a detail window used to display account details and 
    perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)
    def __init__(self, account: BankAccount) -> None:
        """Initializes a new instance of the AccountDetailsWindow class.
        
        Args:
            account (BankAccount): The bank account to be displayed.
        returns:
            None
        """

        super().__init__()

        if not isinstance(account, BankAccount):
            self.reject()
            return
        
        self.account = copy.copy(account)
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"{self.account.balance:.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self):
        """Handles deposit and withdrawal transactions"""
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Deposit Failed", "Amount must be numeric.")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            return

        sender = self.sender()
        transaction_type = ""
        try:
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
            else:
                return  
            
            self.balance_label.setText(f"${self.account.balance:.2f}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            self.balance_updated.emit(self.account)
        
        except Exception as e:
            QMessageBox.critical(self,"Transaction Failed",
                f"{transaction_type} failed: {str(e)}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

        
    @Slot()
    def __on_exit(self):
        """closes the dialog box"""
        self.close()