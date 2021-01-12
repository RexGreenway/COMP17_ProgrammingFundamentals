# IMPORTS #
import random as r
from datetime import date

### BASIC ACCOUNT CLASS ###
class BasicAccount:
    # Account No. counter
    counter = 0

## INITIALISER ##
    def __init__(self, acName, openingBalance):
        # Increment counter with each initialisation
        BasicAccount.counter += 1

        # Intialise input arguments
        self.name = acName
        self.balance = openingBalance

        # Define instance specific variables
        self.acNum = BasicAccount.counter
        self.cardNum = r.randint(0, 9999999999999999)

        # Set exp. date as 3 years from first instance of the account.
        self.cardExp = (int(date.today().strftime("%m")), int(date.today().strftime("%y")) + 3)

## METHODS ##
    # Cast to str output.
    def __str__(self):
        return "Account Details\n- Name: {self.name}\n- Balance: £{self.balance}".format(self=self)

    # Deposit
    def deposit(self, amount):
        self.balance += amount

    # Withdraw
    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print(self.name + " has withdrew £" + str(amount) + ". New balance is £" + str(self.balance) + ".")
        else:
            print("Can not withdraw £" + str(amount))


    # Get Available Balance
    def getAvailableBalance(self):
        return self.balance
    
    # Get Balance
    def getBalance(self):
        return self.balance

    # Print Balance
    def printBalance(self):
            print("Balance: £" + str(self.balance))

    # Get Account Name
    def getName(self):
        return self.name

    # Get Account Number
    def getAcNum(self):
        return str(self.acNum)

    # Issue New Card
    def issueNewCard(self):
        # Generates new cardNum and sets expiry to 3 years from new card issue.
        self.cardNum = r.randint(0, 9999999999999999)
        self.cardExp = (int(date.today().strftime("%m")), int(date.today().strftime("%y")) + 3) 
    
    # Close Account
    def closeAccount(self):
        # Overdrawn check.
        if (self.balance > 0):
            self.withdraw(self.balance)
            return True
        else:
            # Using absolute value scales to represent negative values.
            print("Can not close account due to customer being overdrawn by £" + str(abs(self.balance)))
            return False



### PREMIUM ACCOUNT CLASS (PARENT: BasicAccount) ###
class PremiumAccount(BasicAccount):
## INITIALISER ##
    # Inherit parent variables and initialise new ones.
    def __init__(self, acName, openingBalance, initialOverdraft):
        super().__init__(acName, openingBalance)
        self.overdraft = True
        self.overdraftLimit = initialOverdraft
       
## CHILD-SPECIFIC METHODS ##
    # Set new Overdraft details.
    def setOverdraftLimit(self, newLimit):
        if (newLimit == 0):
            self.overdraft = False
        else:
            self.overdraftLimit = True
        self.overdraftLimit = newLimit

## OVERWRITTEN METHODS ##
    # Cast to str output.
    def __str__(self):
        self.availableBalance = self.balance + self.overdraftLimit
        return "Account Details\n- Name: {self.name}\n- Available Balance: £{self.availableBalance} \n- Overdraft: £{self.overdraftLimit}".format(self=self)

    # Withdraw.
    def withdraw(self, amount):
        if (amount <= self.balance + self.overdraftLimit):
            self.balance -= amount
            print(self.name + " has withdrew £" + str(amount) + ". New balance is £" + str(self.balance) + ".")
        else:
            print("Can not withdraw £" + str(amount))

    # Available Balance (inc. overdraft).
    def getAvailableBalance(self):
        return self.balance + self.overdraftLimit

    # Print Balance (indicating overdraft details). 
    def printBalance(self):
        print("Balance: £" + str(self.balance))
        print("Overdraft: £" + str(self.overdraftLimit))
        print("Available Balance: £" + str(self.balance + self.overdraftLimit))

test = PremiumAccount("Rex", 100, 50)
print(str(test))
print(test.cardNum, test.cardExp)
test.issueNewCard()
print(test.cardNum, test.cardExp)
