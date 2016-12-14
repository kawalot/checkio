
#What is the power hidden within indexes?
def index_power(array, n):
    try:
        return array[n]**n
    except:
        return -1
    return None
print(index_power([65,18,93,94,36,21,65,95,30,43],6))