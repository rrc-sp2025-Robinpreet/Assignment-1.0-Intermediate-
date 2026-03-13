__author__ = "Robinpreet Kaur"
__version__ = "1.0.0"

from datetime import date 


class BankAccount:
    """
    BankAccount class: Maintain bank account data.
    """
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initializes class attributes to argument values.

        Args:
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number representing the account holder.
            balance (float): The current balance of the bank account.
        
        Returns:
            None
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number should be integer.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number should be an integer.")
        
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

        # date_created
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()
        # Strategy pattern attribute
        self._service_charge_strategy = None

    
    @property
    def account_number(self) -> int:
        """
        Accessor for account_number attribute.

        Returns:
            int: The bank account number.
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for client_number attribute.

        Returns:
            int: The client number of account owner.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for balance attribute.

        Returns:
            float: The current balance of the bank account.
        """
        return self.__balance
    # assignment2
    @property
    def date_created(self) -> date:
        """
        Accessor for date_created attribute.

        """
        return self._date_created
    
    def update_balance(self, amount: float):
        """
        Mutator for updating the balance by adding amount.

        Args: 
            amount (float): The amount to update the balance.

        Returns: 
            None
        """
        try:
            self.__balance += float(amount)
        except Exception:
            pass
    
    def deposit(self, amount: float):
        """
        Deposits the amount into the bank account.

        Args:
            amount (float): The amount to deposit. 

        Returns:
            None

        Raises:
            ValueError:
                - If amount is not numeric.
                - If amount is not positive.
        """
        try:
            amount = float(amount)
        except Exception:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """
        Withdraw money from the bank account but the amount must be numeric, positive,
         and must not exceed the current account balance.

        Args:
            amount (float): The amount that needs to withdraw.
        
        Raises:
            ValueError: If amount is not numeric.
            ValueError: If amount is not positive.
            ValueError: If amount exceeds the current balance.
        """

        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdraw amount: {formatted_amount} must be positive.")
        
        if amount > self.__balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self.__balance:,.2f}"
            raise ValueError(
                f"Withdraw amount: {formatted_amount} must not exceed the account balance: {formatted_balance}."
            )
        
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        """
         calculate and return the service charges for the bank account.
     
         Returns:
            float: The service charges for this account.
        """

        if self._service_charge_strategy:
            return self._service_charge_strategy.calculate_service_charges(self)

        return 0.0

        
    def __str__(self):
        """
        Return a string representation of the account with formatted balance.
        """
        
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}\n"  
    