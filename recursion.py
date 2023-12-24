def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


kek = 223
countdown(kek)
print('Countdown done... \n Enter your name now -> ')
imechko = "Obama"  # input()


def greet(name):
    print("Hello O" + name + "!")
    greet2(name)
    print("Getting ready to say bye...")
    bye(name)


def greet2(name):
    print("How are you, " + name + "?")


def bye(name):
    print("Ok, bye!")


greet(imechko)
print("Program done, go to factorial now")


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


y = 15
print("Factorial of " + str(y) + " equal " + str(fact(y)))
kek = [21, 22, 332, 23, 23, 23, 22, 23]


def count_array_elements(arr):
    if not arr:
        return 0
    else:
        return 1 + count_array_elements(arr[1:])


print("lel array length")
print(count_array_elements(kek))


def recursion_binary_search(arr, index0, indexn, val):
    if (indexn < index0):
        return None
    else:
        mid = index0 + ((indexn - index0) // 2)
        if arr[mid] > val:
            return recursion_binary_search(arr, index0, mid-1, val)
        elif arr[mid] < val:
            return recursion_binary_search(arr, mid+1, indexn, val)
        else:
            return mid


kek = [1, 2, 3, 4, 5, 6, 7, 8, 12, 14, 17, 22, 33, 34, 37, 78, 88, 89, 92, 100]
print("binary recursion")
print(recursion_binary_search(kek, 0, len(kek), 17))

