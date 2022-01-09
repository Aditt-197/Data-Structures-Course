def mergeSortedArrays(arr1, arr2):
    newArr = []
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1+arr2

    index1 = 0
    index2 = 0

    while (index1 < len(arr1)) and (index2 < len(arr2)):
        if arr1[index1] <= arr2[index2]:
            newArr.append(arr1[index1])
            index1 += 1
        elif arr1[index1] > arr2[index2]:
            newArr.append(arr2[index2])
            index2 += 1

    return newArr + arr1[index1:] + arr2[index2:]

#Alternative method (The Better Way with Python)

# def mergeSortedArrays(arr1, arr2):
#
#     newArr = arr1 + arr2
#     newArr.sort()
#     return newArr

x = [1, 3, 4, 6, 20]
y = [2,3,4,5,6,9,11,76]
newS = mergeSortedArrays(x,y)

print(newS)