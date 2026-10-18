class Bank_Account: #Creates a class called Bank_Account
  def __init__(self, account_number, balance=0): #Initializes the class with account_number and balance attributes
    self.__account_number = account_number
    self.__balance = balance

  @property # @property decorator is used to define getter, setter, and deleter methods for the private attributes
  def account_number(self): # "def" Defines the function that returns the value of the private attributes.
    return self.__account_number

  @property
  def balance(self):
    return self.__balance

  @account_number.setter # Setter refers to the method that sets the value of the private attribute
  def account_number(self, number):
    self.__account_number = number

  @balance.setter
  def balance(self, amount):
    if amount < 0: #Value of the balance attribute cannot be negative
      raise ValueError("Balance cannot be negative") #Indicates whether the value of the balance attribute is negative.
    self.__balance = amount #Declares the value of the balance attribute to be equal to the amount parameter.

  # ---Example output---
account = Bank_Account("263472", 100000)
account.balance = 100000
account.account_number = "263472"
print(f"Account balance: {account.balance}\nAccount number: {account.account_number}")



