"""
Author: Daniel Montague
Date: 1/20/2026
Assignment: Lab 02 Part B Clemson Market
Course: 1051
Lab Section: 002

Description: This short program calculates the total for an order placed by the user and calculates the tax as 
             defined by the user.
"""


#Variables
price_chips = 5.99
price_sandwich = 13.23
price_bananas = 2.73
num_chips = 0
num_sandwich = 0
weight_bananas = 0.0
total_no_tax = 0.0
tax_rate = 0.0
total_with_tax = 0.0

print("Welcome to the Clemson Market!")

print("We have the following items available:\n")
print("Bag of Chips: $5.99 each")
print("Turkey Sandwich: $13.23 each")
print("Bananas: $2.73 per lb")

#Get user inputs
print("\nHow many bags of chips do you want?", end=" ")
num_chips = int(input())

print("\nHow many turkey sandwiches do you want?", end=" ")
num_sandwich = int(input())

print("\nHow many lbs of bananas do you want?", end=" ")
weight_bananas = float(input())

# Calculate the total without and with taxes and the output both
total_no_tax = (num_chips * price_chips) + (num_sandwich * price_sandwich) + (weight_bananas * price_bananas)
print(f"\nYour total before tax is ${total_no_tax:.2f}.")

print("\nPlease enter the tax rate: ", end="")
tax_rate = float(input())

total_with_tax = ((tax_rate / 100) * total_no_tax) + total_no_tax
print(f"\nYour total after tax is ${total_with_tax:.2f}. Thank you for shopping at the Clemson Market!")