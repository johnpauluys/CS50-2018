# filename: crack.py
""" Attempts to crack a password based on DES algorithm """
import crypt
import sys

# create alphabet variable and set max password length
abc = ([str(chr(n + 65)) for n in range(26)] +
       [str(chr(n + 97)) for n in range(26)])
max_length = 5

# check command line arguments
if len(sys.argv) != 2:
    # print usage to screen and exit if args are invalid
    print("Usage: python {} HASH".format(sys.argv[0]))
    sys.exit(1)
else:
    # set hashsum variable to command line argument
    hashsum = str(sys.argv[1])


def crack(pw_length):
    """ start cracking process, limiting length to max_length value """
    for l in range(pw_length + 1):
        if l == 0:
            # start new string
            key = [''] * (pw_length + 1)
        # generate strings for testing
        run_thru(abc, l, pw_length, key)


def run_thru(letters, lvl, dpth, key):
    """
    generate strings and check password at end of string

    letters = string of all possible characters
    lvl = current string index (should be smaller than dpth)
    dpth = max pw length
    key = generated string/word to check against
    """

    for a in letters:
        key[lvl] = a
        # detect if string's end is reached for checking
        if lvl == dpth:
            # check pw at string's end
            check_pw(''.join(key), hashsum)

        elif key[lvl] != abc[-1]:
            # if last possible character has been reached,
            # without matches, recur
            run_thru(letters, lvl + 1, dpth, key)


def check_pw(word, hash):
    """ check hash against given word and exit if match is found """
    if crypt.crypt(word, hash[:2]) == hash:
        print(word)
        sys.exit(0)


# start program
for char in range(max_length):
    crack(char)