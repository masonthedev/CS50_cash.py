# CS50_cash.py

cash.py is an upodated implementation of a program i wrote in C that was supposed to take a dollar amount and convert that using a greedy algorithm to identify the least amount of coins required to issue change. 

# Change Calculator

This Python program takes an input representing an amount of change in dollars and cents and calculates the minimum number of coins required to make up that amount of change.

## Usage

To run the program, simply execute the Python script in your terminal or IDE. You will be prompted to enter the amount of change. The program will then output the total number of coins required to make up that amount of change, considering quarters, dimes, nickels, and pennies.

python cash.py

# How it Works
The program prompts the user to input an amount of change in dollars and cents.
It then converts the input into an integer representing the total number of cents.
The program then calculates the number of quarters, dimes, nickels, and pennies required to make up that amount of change using a series of while loops.
Finally, it calculates the total number of coins required and prints the result.

# Example 
python cash.py
Change: 1.43
7

Requirements
Python 3.x
cs50 library (install using pip install cs50)

This project is licensed under the MIT License - see the LICENSE file for details.


