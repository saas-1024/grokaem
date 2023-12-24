from random import *
import numpy as np


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array)//3]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]

        #  return quicksort(less) + [pivot] + quicksort(greater)
        return np.concatenate((quicksort(less), [pivot], quicksort(greater)), axis=None)


kek = [23, 213, 8, 22, 43, 22, 11, 8, -11, -22, -188, 188, 1009, 240, -89, 108, 214, 377, -755, 612, -411]
print(quicksort(kek))

