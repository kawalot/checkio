#How to sort an array by absolute values.


def checkio(numbers_array):
    newlist = []
    newlist = sorted(numbers_array, key=abs)
    return newlist


print(checkio([-20, -5, 10, 15]))
print(checkio((1, 2, 3, 0)))
print(checkio((-1, -2, -3, 0)))