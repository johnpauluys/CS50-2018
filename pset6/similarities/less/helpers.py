from nltk.tokenize import sent_tokenize


def compare(a, b):
    """Compare two lists and return a list containing similarites"""

    # initiate empty list to return
    c = []

    # iterate over each line in a, check if it's in b
    # if the line happens to be in b, add it to c
    for line in a:
        if line in b:
            c.append(line)
    return c


def lines(a, b):
    """Return lines in both a and b"""

    # split lines and remove duplicates (set())
    a, b = set(a.split('\n')), set(b.split('\n'))

    return compare(a, b)


def sentences(a, b):
    """Return sentences in both a and b"""

    # create a list of english sentences for each file
    a = set(sent_tokenize(a, language='english'))
    b = set(sent_tokenize(b, language='english'))

    return compare(a, b)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # get substrings before comparing a and b
    a = get_substrings(a, n)
    b = get_substrings(b, n)

    return compare(a, b)


def get_substrings(text, n):
    """ Return substrings of length of given text """

    # initialise empty substrings list
    substrings = []
    # add substrings of length n to 'substrings' list
    for c in range(len(text) - (n - 1)):
        substrings.append(text[c:c + n])

    return set(substrings)