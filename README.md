# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Robinpreet Kaur

## Assignment

Assignment-1: Develop a robust and flexible Bank Account and Client classes to serve as a solid foundation for the evolving needs of banking system, ensuring it can handle a variety of banking transactions securely and efficiently.

Assignment-2: Applying object oriented Design. This assignment will extend the  BankAccount class created in previous assignment.
BankAccount class will be used as a superclass from which more specific subclasses will be derived.

Assignment-3: In Assignment-3 we used the stratergy and observer patterns.

Stratergy: The computation of service fees for various kinds of bank accounts is handled by the Strategy Pattern.
The service charge logic has been implemented within each BankAccount subclass, rather than directly.
shifted to distinct strategy courses. Each approach has a unique algorithm for determining service fees.

Observer: The Observer Pattern is used to notify bank clients when significant events occur on their accounts.
The BankAccount class acts as the Subject and maintains a list of observers. The Client class acts
as the Observer and receives notifications when the account state changes.

## Encapsulation


Encapsulation in the BankAccount class means keeping the account data safe.
The data attributes (account_number, client_number, and balance) are made private, so they cannot be changed directly from outside the class.

## Polymorphism

Polymorphism is when different classes can used same method name, but each class does something different.
In this project, "ChequingAccount", and "SavingsAccount", and "InvestmentAccount" will have their own version of the "get_service_charges()" method.

## Assignment-4 

## Event-Driven Programming Paradigm

- A **balance_updated signal** is released with the updated `BankAccount` object whenever a transaction takes place in `AccountDetailsWindow`.

- Using the `update_data` slot, `ClientLookupWindow` responds to this signal by updating the CSV file, internal data structures, and Gui table.