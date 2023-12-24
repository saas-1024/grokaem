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


def sum_array(arr):
    total = 0
    for i in arr:
        total += i
    return total


print("ass")
print(sum_array(kek))


def count_array_elements(arr):
    total = 0
    if arr == []:
        return 0
    else:
        for i in arr:
            total += 1
    return total


pep = []
print("len of array func")
print(count_array_elements(kek))
print(count_array_elements(pep))


def max_element_of_list(arr):
    buffer = arr[0]
    for i in arr:
        if i > buffer:
            buffer = i
    return buffer


print(str("max element is ") + str(max_element_of_list(kek)))
