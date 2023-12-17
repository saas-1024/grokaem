kek = [1, 2, 3, 4, 5, 6, 7, 8, 12, 14, 17, 22, 33, 34, 37, 78, 88, 89, 92, 100]


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


result = binary_search(kek, 22)
print("Index of element is " + str(result))
