#How to work with arrays indexes.
def checkio(array):
    try:
        result = 0
        length = len(array)
        for i in range(0,length,2):
            result = result + array[i]
        return result * array[length-1]
    except:
        return 0
print(checkio([0, 1, 2, 3, 4, 5]))