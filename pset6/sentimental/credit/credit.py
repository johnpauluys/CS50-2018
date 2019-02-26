# filename: credit.py
""" Get user input (credit card number) and validate if the card is legit.
    Also print which credit card company the card belongs to.
"""
# get user input and validate given input
while True:
    try:
        cc_number = int(input("Number: "))
    except ValueError:
        continue
    if cc_number >= 0:
        break

# change cc_number to string for indexing
cc_number = str(cc_number)
num_length = len(cc_number)

# get sum of every other number multiplied by 2, starting from the back
sum_1 = 0
for i in range(2, num_length + 1, 2):
    digit = int(cc_number[-i]) * 2
    # check if multiplied number is more than a digit long
    # if so, add each digit to sum_1, if not, add digit to sum_1
    if len(str(digit)) > 1:
        for j in range(len(str(digit))):
            sum_1 += int(str(digit)[j])
    else:
        sum_1 += int(digit)

# get sum of every other number that wasn't multiplied
sum_2 = 0
for i in range(1, num_length + 1, 2):
    sum_2 += int(cc_number[-i])

# check if card number is valid by using % or just by checking if last digit == 0
if (sum_2 + sum_1) % 10 == 0:
    amex = (34, 37)
    master = (51, 52, 53, 54, 55)

    # find which credit company the card belongs to
    if int(cc_number[:2]) in amex and num_length == 15:
        print("AMEX")
    elif int(cc_number[:2]) in master and num_length == 16:
        print("MASTERCARD")
    elif int(cc_number[0]) == 4 and num_length == 13 or num_length == 16:
        print("VISA")
    else:
        print("INVALID")
else:
    print('INVALID')