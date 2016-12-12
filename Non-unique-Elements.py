#Trim an array down to its non-unique elements

list1 = [1, 2, 3, 1, 3]
list2 = [1, 2, 3, 4, 5]
list3 = [5, 5, 5, 5, 5]
list4 = [10, 9, 10, 10, 9, 8]

def checkio(listin):
    listout = []
    for i in listin:
        if listin.count(i) > 1:
            listout.append(i)
    return listout

print (checkio(list1))
print (checkio(list2))
print (checkio(list3))
print (checkio(list4))