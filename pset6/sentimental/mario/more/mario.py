# filename: mario.py
""" Display mario's pyramid of n size """

# get positive int from user
while True:
    # prompt user for a number, check if input is valid
    try:
        height = int(input("Height: "))
    except ValueError:
        continue
    if height >= 0 and height <= 23:
        break

for i in range(height):
    # print whitespace
    for j in range((height - i) - 1):
        print(' ', end='')

    # print left side of pyramid
    for j in range(i + 1):
        print('#', end='')

    # add a gap of two spaces
    print('  ', end='')

    # print right side of pyramid
    for j in range(i + 1):
        print('#', end='')

    # new line
    print()