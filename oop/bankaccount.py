from abc import ABC , abstractmethod 

'''
CLASS : BLUEPRINTS -> MEANT TO CREATE OBJECTS : instansiated 
ABC : this makes a class abstract/interface i.e. means it will define methods 
, methods must be implemented in any class that will now inherit the bankaccount


'''
class BankAccount(ABC):
    def __init__(self, account_number):
        self.account_number = account_number
        self._balance = 0.0
        self.owners = [] # many to many relationship : Joint account
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be greater than zero")
        
    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds")
            
    def get_balance(self):
        return self._balance
    
    def add_owner(self,customer):
        if customer not in self.owners:
            self.owners.append(customer)
            print(f"{customer.name} added as an owner to account {self.account_number}")
            
    @abstractmethod
    def account_type(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name 
        self.accounts = []
        
    def add_account(self, account: BankAccount):
        if account not in self.accounts:
            self.accounts.append(account)
        
    def list_account(self):
        print(f"Accounts for {self.name}:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.get_balance()}")
        return [account.account_number for account in self.accounts]
    
class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
    
    def add_customer(self, customer):
        # how can i ensure the validity of the customer object? 
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer object")
        self.customers.append(customer)
    
    def find_customer_by_name(self,name):
        for cust in self.customers:
            if cust.name.lower() == name.lower():
                return cust
            return None 
        
    def list_all_customers(self):
        return [customer.name for customer in self.customers]



 
        
class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate = 0.02):
        # why is the super() method used here?
        super().__init__(account_number)
        self.interest_rate = interest_rate
    
    def account_type(self):
        return "Savings account"
    
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest added: {interest}. New balance: {self._balance}")
    
class CheckingAccount(BankAccount):
    def __init__(self, account_number, overdraft_limit = 100.0):
        
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit
        
    #polymorphism
    def withdraw(self,amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded")
            
    
    def account_type(self):
        return "Checking account"
    

def run_bank_test():
    print("Welcome to the Bank!")
    bank = Bank("My Bank")
    #create customers 
    joseph = Customer("Joseph")
    jane = Customer("Jane")
    # add customers to the bank 
    bank.add_customer(joseph)
    bank.add_customer(jane)
    #create the accounts 
    joseph_savings = SavingsAccount("123456789")
    jane_checking = CheckingAccount("987654321")
    # joint account 
    both_joint = SavingsAccount("111111111")
    ## assigning accounts to the oweners 
    joseph.add_account(joseph_savings)
    jane.add_account(jane_checking)
    # one to many relationship 
    # savings account 'has a' -> one to many relationship with customers 
    joseph.add_account(both_joint)
    jane.add_account(both_joint)
    # perform operations
    # deposits and interest 
    joseph_savings.deposit(1000)
    jane_checking.deposit(500)
    joseph_savings.add_interest()
    # withdraw 
    jane_checking.withdraw(600)
    both_joint.withdraw(300)
    
    # list accounts 
    print("accounts")
    bank.list_all_customers()
    
print(run_bank_test())
    