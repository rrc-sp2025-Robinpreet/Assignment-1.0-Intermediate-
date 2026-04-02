"""Defines the ClientLookupWindow class."""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot 
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

class ClientLookupWindow(LookupWindow):
    """Represents a main window for looking up BankAccounts.""" 
    def __init__(self):
        super().__init__()

        clients, accounts = load_data()
        self.client_listing = clients
        self.accounts = accounts

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)  

    @Slot()
    def __on_lookup_client(self):
        """Handling lookup button clicked."""
        client_number_text = self.client_number_edit.text().strip()

        try:
            client_number = int(client_number_text)
        except ValueError:
            self.reset_display()
            QMessageBox.warning(self,"Non-Numeric Client","Client number must be a numeric value.")
            return
        
        if client_number not in self.client_listing:
            self.reset_display()
            QMessageBox.information(self,"Client Not Found",
                f"Client with number: {client_number} not found.")
            return
        
        client = self.client_listing[client_number]
        client_name = f"{client.first_name} {client.last_name}"
        self.client_info_label.setText(client_name)
        self.account_table.setRowCount(0)

        row = 0
        for account in self.accounts.values():

            if account.client_number == client_number:

                self.account_table.insertRow(row)

                item_number = QTableWidgetItem(str(account.account_number))
                item_number.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 0, item_number)

                item_balance = QTableWidgetItem(f"${account.balance:,.2f}")
                item_balance.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, item_balance)

                item_date = QTableWidgetItem(str(account.date_created))
                item_date.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 2, item_date)

                item_type = QTableWidgetItem(account.__class__.__name__)
                item_type.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 3, item_type)

                row += 1

        self.account_table.resizeColumnsToContents()

