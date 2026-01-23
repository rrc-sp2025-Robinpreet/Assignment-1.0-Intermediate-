
## Author:Robinpreet Kaur
## Version:1.0.0

from email_validator import validate_email, EmailNotValidError

class Client:
    """ 
    Client class: Maintain client data.
    """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes class attributes to argument values.

        Args:
            client_number (int): Client number. 
            first_name (str): First name of the client.
            last_name (str): Last name of the client.
            email_address (str): Email address of the client.

        Returns:
            None
        
        Raises:
            ValueError: When client_number is not an integer,
                        when first_name is blank,
                        when last_name is blank.
        
        """
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number should be an integer.")
        
        # validate first name
        if isinstance(first_name, str) and len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        
        # validate last name 
        if isinstance(last_name, str) and len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")
        
        #email validator
        email = "email@pixell-river.com"
        
        try:
            validate_email(email_address, check_deliverability=False)
            self.__email_address = email_address
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Accessor for client_number attribute.

        Returns:
            int: The client number 
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for first_name attribute.

        Returns:
            str: The first name of the Client.
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for last_name attribute.

        Returns:
            str: The last name of the client.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for email_address attribute.

        Returns:
            str: The email address of the client.
                Default set to "email@pixell-river.com" if it is invalid.
        """
        return self.__email_address
    
    def __str__(self) -> str:
        """
        Returns a string of the client object.

        Returns:
            str: A formatted string of client details.
        """
        return f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.email_address}\n"
    