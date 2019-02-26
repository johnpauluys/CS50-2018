from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    # calc lengths of given strings
    len1, len2 = len(a), len(b)

    # create empty 2D list
    matrix = []
    for i in range(len1 + 1):
        matrix.append([])
        for j in range(len2 + 1):
            matrix[i].append([])

    # add base values
    matrix[0][0] = (0, None)
    # set values for first row and first column
    for i in range(1, len1 + 1):
        matrix[i][0] = (i, Operation.DELETED)
    for j in range(1, len2 + 1):
        matrix[0][j] = (j, Operation.INSERTED)

    # fill out the rest of the table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            # check if compared chars are equal, use lowest value
            if a[i - 1] == b[j - 1]:
                data = (matrix[i - 1][j - 1][0], 'S')
            # if not, calc optimal value
            else:
                data = min(
                    (matrix[i - 1][j][0] + 1, 'D'),
                    (matrix[i][j - 1][0] + 1, 'I'),
                    (matrix[i - 1][j - 1][0] + 1, 'S'))

            # set operation
            if data[1] == 'D':
                matrix[i][j] = (data[0], Operation.DELETED)
            elif data[1] == 'I':
                matrix[i][j] = (data[0], Operation.INSERTED)
            else:
                matrix[i][j] = (data[0], Operation.SUBSTITUTED)

    return matrix
