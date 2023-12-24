def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


kek = [1,7,8,3,5,9,100,56,-12,22,-16,33,234,11,267,-22,-345,-10,22,12]
cyka = findSmallest(kek)
print(selectionSort(kek))

