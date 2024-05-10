from cs50 import get_float

while True:
    cents = round(get_float("Change: ") * 100)
    if cents > 0:
        break

# Calculate Quarters
quarters = 0
while cents >= 25:
    quarters += 1
    cents = cents - 25

# Calculate Dimes
dimes = 0
while cents >= 10:
    dimes += 1
    cents = cents - 10

# Calculate Nickles
nickels = 0
while cents >= 5:
    nickels += 1
    cents = cents - 5

# Calculate Pennies
pennies = 0
while cents >= 1:
    pennies += 1
    cents = cents - 1


# Calculate total coins
total_coins = quarters + dimes + nickels + pennies
print(total_coins)
