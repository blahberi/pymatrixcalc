import numpy as np


def CutArray(arr, pos):
    cutArray = np.array(arr)
    cutArray = np.delete(cutArray, pos[0], 1)
    cutArray = np.delete(cutArray, pos[1], 0)
    return cutArray


def calc_det(arr):
    if isinstance(arr, int) == True or len(arr) == 1:
        return int(arr)
    modifiedArray = np.array(arr)
    detData = 0
    isNegative = False
    for i in range(len(modifiedArray[0])):
        if isNegative == True:
            modifiedArray[0, i] = -1 * modifiedArray[0, i]
            isNegative = False
        else:
            isNegative = True
    for i in range(len(modifiedArray[0])):
        cutArray = modifiedArray
        cutArray = np.delete(cutArray, 0,0)
        cutArray = np.delete(cutArray,i,1)
        if len(cutArray) == 1:
            detData = detData + modifiedArray[0, i] * cutArray[0]
        if len(cutArray) > 1:
            detData = detData + modifiedArray[0, i] * calc_det(cutArray)
    return int(detData)


def print_matrix(arr):
    for i in arr:
        print(i)


def find_adjoint(arr):
    modifiedArray = np.array(arr)
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            modifiedArray[x, y] = calc_det(CutArray(arr, [y, x]))

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if (x + y) % 2 != 0:
                modifiedArray[x, y] = modifiedArray[x, y] * -1

    done = []
    for x in range(len(modifiedArray)):
        for y in range(len(modifiedArray[y])):
            if [x, y] not in done:
                temp = modifiedArray[x, y]
                modifiedArray[x, y] = modifiedArray[y, x]
                modifiedArray[y, x] = temp
                done.append([y, x])
    adjointArray = modifiedArray
    return adjointArray


def calc_inverse(arr):
    arrDet = calc_det(arr)
    arrAdj = find_adjoint(arr)
    arrInverse = arrAdj / arrDet
    return arrInverse