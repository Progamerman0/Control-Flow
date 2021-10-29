"""
Programer: Spencer Kohler
Date: 10-11-2021
Program: ATM Bank Transaction

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


    #This part of the program will ask users to complete a transaction through the ATM
    print("Please insert your card\n")
    print("Welcome to Cash-R-Us ATM", firstName, lastName, "\n")
    userPIN = input("Enter your PIN: ")

    if userPIN == pin:
        balance = 100000
        print("Your balance: $" + str(balance))

        #Ask users what kind of transaction they want
        typeOfTransaction = input("Would you like to deposit or or withdrawl\nW = withdrawal, D = deposite, or B = balance: ").lower()
        
        if typeOfTransaction == "w":
            withdrawlAmount = int(input("How much do you wish to withdrawl: "))
            balance = balance - withdrawlAmount
            print("Your new balance is: $" + str(balance))
        
        elif typeOfTransaction == "d":
            depositAmount = int(input("How much do you want to deposit: "))
            balance = balance + depositAmount
            print("Your new balance is: $" + str(balance))

        else:
            print("Your current balance is: $" + str(balance))

    else:
        print("Sorry", firstName, lastName, "your PIN dosen't match our records.")


else:
    print("Have a great day", firstName, lastName + ", please come and visit soon.")