"""A program to demonstrate your understanding of the Observer Pattern.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

# 1.  Import all BankAccount types using the bank_account package
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client
from datetime import date

# 2. Create a Client object with data of your choice.
client = Client(101, "Roop", "Pannu", "roop.pannu@example.com")


# 3a. Create a ChequingAccount object with data of your choice, using 
#   the client_number of the client created in step 2.

chequing_account = ChequingAccount(
    account_number=2006,
    client_number=client.client_number,  
    balance=500.00,
    date_created="2026-02-02",
    overdraft_limit=-200.0,
    overdraft_rate=0.05
)

# 3b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in step 2.
savings_account = SavingsAccount(
    account_number=3007,
    client_number=client.client_number,  # Use client_number from Client
    balance=1500.00,
    date_created="2026-02-03",
    minimum_balance=100.0
)


# 4. The ChequingAccount and SavingsAccount objects are 'Subject' 
# objects. The Client object is an 'Observer' object.  
# 4a. Attach the Client object (created in step 1) to the 
#   ChequingAccount object (created in step 2).
chequing_account.attach(client)

# 4a. Attach the Client object (created in step 1) to the 
#   SavingsAccount object (created in step 2).
savings_account.attach(client)

# 5a. Create a second Client object with data of your choice.
second_client = Client(202, "Jordan", "Taylor", "jordan.taylor@example.com")
  
# 5b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in this step.
second_savings_account = SavingsAccount(
    account_number=4008,
    client_number=second_client.client_number,  # Use client_number from second_client
    balance=2500.00,
    date_created="2026-02-01",
    minimum_balance=200.00
)

second_savings_account.attach(second_client)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and 
# withdraws) which would cause the Subject (BankAccount) to notify the 
# Observer (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    chequing_account.deposit(15000.00)
    chequing_account.withdraw(1000.0)
    chequing_account.deposit(3000.0)
except Exception as e:
    print(f"chequing account transaction error: {e}")

try:
    savings_account.deposit(350.0)
    savings_account.withdraw(170.0)
    savings_account.withdraw(2500.0)
except Exception as e:
    print(f"Savings account transaction error: {e}")

try:
    second_savings_account.withdraw(600.0)
    second_savings_account.deposit(250.0)
    second_savings_account.withdraw(300.0)
except Exception as e:
    print(f"Savings second_savings_account error: {e}")

print(chequing_account)
print()
print(savings_account)
print()
print(second_savings_account)

print("\n---Transactions Completed --\n")

