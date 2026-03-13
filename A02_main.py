"""A program to demonstrate the use of the BankAccount subclasses.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
def main():

    try:
        chequing_account = ChequingAccount(
            2006,
            411,
            -200.0,
            date(2025, 10, 3),
            -100.0,
            0.05
        )
    except Exception as e:
        print(e)

   


# 3. Print the ChequingAccount created in step 2.

try:
        print(chequing_account)
except Exception as e:
        print(e)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
        print(chequing_account)
        print("Service Charges:", round(chequing_account.get_service_charges(), 2))
except Exception as e:
        print(e)



# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
try:
        chequing_account.deposit(400.0)
        print("Deposit successful.")
except Exception as e:
        print(e)

# 4b. Print the ChequingAccount
try:
        print(chequing_account)
except Exception as e:
        print(e)


# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

try:
        print("Service Charges:", round(chequing_account.get_service_charges(), 2))
except Exception as e:
        print(e)



print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
        savings_account = SavingsAccount(
            3001,             
            2001,             
            600.0,            
            date(2024, 10, 3),
            500.0             
        )
except Exception as e:
        print(e)


# 6. Print the SavingsAccount created in step 5.
try:
        print(savings_account)
except Exception as e:
        print(e)


# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
        print("Service Charges:", round(savings_account.get_service_charges(), 2))
except Exception as e:
        print(e)


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
try:
        savings_account.withdraw(150.0)
        print("Withdrawal successful.")
except Exception as e:
        print(e)


# 7b. Print the SavingsAccount.
try:
        print(savings_account)
except Exception as e:
        print(e)
    

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
        print("Service Charges:", round(savings_account.get_service_charges(), 2))
except Exception as e:
        print(e)


print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
        investment_account = InvestmentAccount(
            4001,               
            3001,                
            10000.0,             
            date(2023, 1, 1),    
            2.50                 
        )
except Exception as e:
        print(e)

# 9a. Print the InvestmentAccount created in step 8.
try:
        print(investment_account)
except Exception as e:
        print(e)


# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
        print("Service Charges:", round(investment_account.get_service_charges(), 2))
except Exception as e:
        print(e)


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
        old_investment_account = InvestmentAccount(
            4002,                
            3002,              
            15000.0,             
            date(2012, 1, 1),    
            2.50                 
        )
except Exception as e:
        print(e)

# 11a. Print the InvestmentAccount created in step 10.
try:
        print(old_investment_account)
except Exception as e:
        print(e)

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
        print("Service Charges:", round(old_investment_account.get_service_charges(), 2))
except Exception as e:
        print(e)


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
print("===================================================")
print("APPLYING SERVICE CHARGES TO ALL ACCOUNTS")


       

accounts = [
        chequing_account,
        savings_account,
        investment_account,
        old_investment_account
    ]

for account in accounts:
    try:
        service_charge = account.get_service_charges()   # polymorphic call
        account.withdraw(service_charge)                 # superclass method
        print(f"Service charge of {service_charge:.2f} withdrawn.")
    except Exception as e:
        print(e)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("===================================================")
print("FINAL ACCOUNT DETAILS")

for account in accounts:
    print(account)
    print()

if __name__ == "__main__":
    main()