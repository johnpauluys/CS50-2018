# filename: cash.py
""" Get amount of change from user input, calculate least amount
    of coins (25c, 10c, 5c, 1c) needed to make up the sum
"""

while True:
    # get user input
    try:
        change = float(input("Change owed: "))
    except ValueError:
        continue
    # check if user input is valid
    if change > 0:
        break

# convert input to cent amount
change = int(round(change, 2) * 100)

# initilize coins counter variable
coins = 0

# calculate amount of coins
for n in [25, 10, 5, 1]:
    # add coins
    coins += change // n
    # subtract coin values from change
    change %= n

# print number of coins to screen
print(coins)