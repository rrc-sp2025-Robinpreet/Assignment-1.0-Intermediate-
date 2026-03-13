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

#     Import date
from datetime import date

#     Import Client
from client.client import Client



# 2. Create a Client object with data of your choice.
client = Client(
    client_number=101,
    first_name="Roop",
    last_name="Pannu",
    email_address="roop.pannu@example.com"
)




# 3a. Create a ChequingAccount object with data of your choice, using 
#   the client_number of the client created in step 2.

chequing_account = ChequingAccount(
    account_number=2006,
    client_number=client.client_number,  
    balance=500.00,
    date_created=date.today(),
    overdraft_limit=-200.0,
    overdraft_rate=0.05
)

# 3b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in step 2.
savings_account = SavingsAccount(
    account_number=3007,
    client_number=client.client_number,  # Use client_number from Client
    balance=1500.00,
    date_created=date.today(),
    minimum_balance=100.0
)


# 4. The ChequingAccount and SavingsAccount objects are 'Subject' 
# objects. The Client object is an 'Observer' object.  


# 4a. Attach the Client object (created in step 1) to the 
#   ChequingAccount object (created in step 2).


# 4a. Attach the Client object (created in step 1) to the 
#   SavingsAccount object (created in step 2).


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in this step.


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and 
# withdraws) which would cause the Subject (BankAccount) to notify the 
# Observer (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
print("\n--- Transactions on ChequingAccount ---")
try:
    # Transaction 1: Large deposit (should notify)
    chequing_account.deposit(15000.00)
except ValueError as e:
    print(f"Error: {e}")

try:
    # Transaction 2: Small withdrawal (should NOT notify)
    chequing_account.withdraw(100.00)
except ValueError as e:
    print(f"Error: {e}")

try:
    # Transaction 3: Large withdrawal (should notify)
    chequing_account.withdraw(12000.00)
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Transactions on SavingsAccount ---")

try:
    # Transaction 1: Small deposit (should NOT notify)
    savings_account.deposit(50.00)
except ValueError as e:
    print(f"Error: {e}")

try:
    # Transaction 2: Large withdrawal (should notify for low balance)
    savings_account.withdraw(1400.00)
except ValueError as e:
    print(f"Error: {e}")

try:
    # Transaction 3: Another withdrawal (should notify again for low balance)
    savings_account.withdraw(100.00)
except ValueError as e:
    print(f"Error: {e}")

