# filename: mario.py
""" Display half pyramid """

# get input from user
while True:
    # prompt user for a number, check if input is valid
    try:
        height = int(input("Height: "))
    except ValueError:
        continue
    # limit user input to positive integers less than 24
    if height >= 0 and height <= 23:
        break

for n in range(height):
    # print whitespace
    for i in range((height - n) - 1):
        print(' ', end='')
    # print brick(s)
    for i in range(n + 1):
        print('#', end='')
    # print one extra brick on each line.
    print('#')