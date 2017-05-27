b = [[6, 6, 7, 4, 4, 6, 7, 9, 7, 9],
     [4, 1, 8, 4, 7, 3, 5, 1, 1, 6],
     [6, 1, 8, 8, 9, 3, 7, 6, 8, 9],
     [8, 8, 7, 1, 6, 2, 1, 4, 1, 6],
     [4, 4, 9, 9, 8, 8, 5, 4, 9, 8],
     [5, 8, 1, 6, 8, 7, 1, 2, 9, 7],
     [1, 8, 2, 7, 8, 9, 8, 1, 7, 1],
     [7, 2, 7, 3, 7, 4, 3, 7, 1, 3],
     [7, 3, 8, 7, 5, 2, 8, 9, 2, 2],
     [5, 6, 4, 3, 1, 5, 5, 9, 2, 9]]

d = [[3, 2, 6, 5, 6, 2, 8, 3, 7, 4],
     [9, 6, 5, 9, 7, 6, 8, 5, 1, 6],
     [8, 6, 2, 6, 1, 9, 3, 6, 6, 4],
     [8, 5, 3, 2, 3, 8, 7, 4, 6, 4],
     [3, 2, 1, 4, 5, 1, 2, 5, 6, 9],
     [4, 5, 8, 7, 5, 5, 8, 4, 9, 5],
     [7, 9, 9, 9, 5, 9, 9, 8, 1, 2],
     [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
     [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
     [4, 8, 1, 4, 5, 8, 8, 7, 4, 7]]

a =[[3, 2, 6, 5, 6, 2, 8, 3, 7, 4],
    [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
    [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
    [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
    [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
    [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
    [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
    [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
    [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
    [4, 8, 1, 4, 5, 8, 8, 7, 4, 7]]

c = [[1, 2],
     [3, 4]]


def checkio(matrix):
    length = len(matrix)
    for line in matrix:
        sem = 0
        for i in range(length-1):
            if line[i] == line[i+1]:
                sem = sem + 1
                if sem >= 3:
                    return True
            else:
                sem = 0
    return False


def diagonal(matrix):
    temp = [[] for i in range(len(matrix))]
    #sem = 0
    for k in range(len(matrix)):
        for i in range(len(matrix)-k):
            temp[k].append(matrix[i+k][i])
    print(temp)        
    for line in temp:
        sem = 0
        length = len(line)
        for i in range(length-1):
            if line[i] == line[i+1]:
                sem = sem + 1
            else:
                sem = 0
        if sem >= 3:
            return True
    return False


def rotate(matrix):
    lenm = len(matrix)
    rotated_matrix = [[] for i in range(lenm)]
    for x in range(lenm):
        for y in range(lenm-1,-1,-1):
            rotated_matrix[x].append(matrix[y][x])
    return rotated_matrix     

if __name__ == '__main__':
    print(checkio(a))
    print(diagonal(a))
    for i in a:
        print(i)
    b = rotate(a)
    print()
    for i in b:
        print(i)
    
    print(checkio(b))

    print(diagonal(b))

    c = rotate(b)
    print(checkio(c))
    print(diagonal(c))