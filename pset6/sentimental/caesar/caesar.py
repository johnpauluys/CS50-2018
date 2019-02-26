# filename: caesar.py
"""
Get cipher code from command line,
print user input (plaintext) in cipher form (ciphertext).
"""
import sys

# check whether command line argument is given
if sys.argv[1].isdecimal():
    # convert command line string to int
    # and use modulo in case the number is larger than 26
    k = int(sys.argv[1]) % 26

    # prompt user for plaintext
    plaintext = str(input("plaintext: "))

    # initialize empty string variable to contain ciphertext
    ciphertext = ''

    # encipher plaintext.
    for c in plaintext:
        # add enciphered alphabetical characters to ciphertext variable
        if c.isalpha():
            if c.isupper():
                ciphertext += chr(((ord(c) - 65 + k) % 26) + 65)
            elif c.islower():
                ciphertext += chr(((ord(c) - 97 + k) % 26) + 97)
        else:
            # add non-alphabetical characters without enciphering
            ciphertext += c
    # display ciphertext
    print('ciphertext:', ciphertext)
else:
    # exit and display program usage to user
    print("Usage:", sys.argv[0], 'k')