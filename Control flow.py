#Programer: Spencer Kohler
#Date: 10-11-2021
#Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing if, elif, and else statements
Nesting if statments and refresh our comparison and logical operators
"""

print("Welcome to Cash R us!\nLet's take a moment to set up your account.\n")

#Set up account by finding the their first and last names using Variables

firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("Welcome to Cash R Us,", firstName, lastName + ", we will now set up a pin for your account.\n")

pin = input("Please choose your PIN: ")

print("\nThank you", firstName + ", we see you set your PIN to", pin)

print("\nWould you like to make a transaction through our ATM?")
atm = input("Yes or No: ").lower()
if atm == "yes":
    print("\n********************************************\n")




else:
    print("Have a great day", firstName, lastName + ", please come and visit soon.")