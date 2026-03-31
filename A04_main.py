"""The PiXELL River Financial Banking System account management 
program.
"""

import sys
from user_interface.client_lookup_window import ClientLookupWindow
from PySide6.QtWidgets import QApplication

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

def main() -> None:
    """The main function."""

    app = QApplication(sys.argv)
    mainWindow = ClientLookupWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
