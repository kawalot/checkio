"""
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.
Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer. 
"""


def safe_pawns(pawns):
    safe = 0
    for elem in pawns:
        left = chr(ord(elem[0]) - 1) + str(int(elem[1]) - 1)
        right = chr(ord(elem[0]) + 1) + str(int(elem[1]) - 1)
        if left in pawns or right in pawns:
            safe += 1
    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
