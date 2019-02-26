import sys

# check whether only a single argument was given
if len(sys.argv) == 2 and sys.argv[1].isalpha():
    # set key variable
    key = sys.argv[1]
    # get and set key_len for better performance
    key_len = len(key)

    # get plaintext string from user
    plaintext = str(input("plaintext: "))

    # initiate enciphering
    print('ciphertext: ', end='')
    # initialize counter
    k_counter = 0
    for c in range(len(plaintext)):
        # encipher alphabetical characters
        if plaintext[c].isalpha():

            # set variable for string indices
            index = k_counter % key_len

            # handle upper and lowercases
            if key[index].isupper():
                k = ord(key[index]) - 65
            else:
                k = ord(key[index]) - 97

            # add enciphered characters to plaintext variable
            if plaintext[c].isupper():
                char = chr((ord(plaintext[c]) - 65 + k) % 26 + 65)
            else:
                char = chr((ord(plaintext[c]) - 97 + k) % 26 + 97)
        # add non-alphabetical without enciphering
        else:
            char = plaintext[c]

        # increment counter
        k_counter += 1

        # print enciphered character
        print(char, end='')
    # new line
    print()

# exit if command line argument is invalid
else:
    print("Usage: python {} KEYWORD".format(sys.argv[0]))
    print("\nPLEASE NOTE:\nKEYWORD should only contain alphabetical characters and no numbers")
    exit(1)