import operator
from heapq import nlargest
from os import listdir
from os.path import isfile, join
import collections

#  task1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
#  end of task 1

#  task 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# #  return mutual
# a1 = set(a)
# b2 = set(b)
# kek = a1.intersection(b2)
# result = [elem for elem in a if elem in b]
# print(result)
# print(kek)
#  end of task 2

#  task 3
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sort1 = sorted(d.items())
# print(sort1)
# sort2 = dict(sorted(d.items(), key=lambda item: item[1]))
# print(sort2)
#  end of task 3

#  task 4
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# #  merge the dicts
# result = {}
# for d in (dict_a, dict_b, dict_c):
#     result.update(d)
# print(d)
# result2 = {**dict_a, **dict_b, **dict_c}
# print(result2)
#  end of task 4

#  task 5
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# #  find the most 3 key values
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)
#
# result_new = nlargest(3, my_dict, key=my_dict.get)
# print(result_new)
#  end of task 5

#  task 6
#  any number in any notation to the string
# number = input()
# print(int('ABC', 16))
#  end of task 6

#  task 7
#  pascal triangle


# def pascal_triangle(rows):
#     row = [1]
#     y = [0]
#     for i in range(max(rows, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
#
# pascal_triangle(20)
#  end of task 7

#  task 8


# def is_palindrome(str):
#     return str == str[::-1]
#
#
# print(is_palindrome('abba'))
# print(is_palindrome('akbar'))
#  end of task 8

#  task 9


# def convert_seconds_to_ddhhmmss(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24*3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f'{days}:{hours}:{minutes}:{seconds}')
#
#
# convert_seconds_to_ddhhmmss(1234567890)
#  end of task 9

#  task 10
# values = input("Input numbers divided by ',' ")
# list_of_ints = values.split(',')
# ints = map(int, list_of_ints)
# lst = list(ints)
# tup = tuple(lst)
# print(lst)
# print(tup)
#  end of task 10

#  task 11
# list = [1,2,3,4,5,6,7,8,9,0]
# print(list[0])
# print(list[-1])
#  end of task 11

#  task 12


# def get_file_extension(filename):
#     filename_parts = filename.split('.')
#     if len(filename_parts) < 2:
#         raise ValueError('file has no extension')
#     first, *middle, last = filename_parts
#     if not first or not last and not middle:
#         raise ValueError('file has no extension')
#     return filename_parts[-1]
#
#
# print(get_file_extension('fjdif.kek'))
# print(get_file_extension('ossdd.kek.'))
# print(get_file_extension('testtestkek'))
#  end of task 12

#  task 13 n+nn+nnn
# n = int(input())
# n1 = n
# n2 = n*n
# n3 = n*n*n
# print(n1+n2+n3)
#  end of task 13

#  task 14
# spisochek = [11, 22, 34, 45, 32, 41, 15, 233, 122, 153, 533, 237, 22, 135, 89, 155]
# for i in spisochek:
#     print(i)
#     if i == 237:
#         break

#  end of task 14

#  task 15
# list1 = [11, 22, 34, 45, 32, 41, 15, 233, 122, 153]
# list2 = [233, 122, 153, 533, 237, 22, 135, 89, 155]
# a = set(list1)
# b = set(list2)
# print(a - b)
#  end of task 15

#  task 16
# dir_show = input()
# files = [f for f in dir_show if isfile(join(dir_show, f))]
# print(files)
#  end of task 16

#  task 17
# number = int(input())
# number_list = [int(i) for i in str(number)]
# print(sum(number_list))
#  end of task 17

#  task 18
# check_str = str(input())
# check_symbol = str(input())
# kek = 0
# for i in check_str:
#     if i == check_symbol:
#         kek += 1
# print(kek)
#  end of task 18

#  task 19
# a = 5
# b = 7
# print(a, b)
# temp = a
# a = b
# b = temp
# print(a, b)
#  end of task 19

#  task 20
# nums = [45, 55, 22, 15, 60, 88, 90, 99]
# result = list(filter(lambda x: not x % 15, nums))
# print(result)
#  end of task 20

#  task 21
# keks = [13265, 84345, 85, 3247, 33, 21, 33245, 32, 324, 56, 653, 5423, 732, 34]
# a = len(keks)
# temp = set(keks)
# b = len(temp)
# if a == b:
#     print("Unique")
# else:
#     print("Not unique")
#  end of task 21

#  task 22
# str = ("dfasdhfj asdijash asid asidasi dasi dasid ias diasd aisdjhias djias djas djiasd jiasj dasd asjdasdas d d d "
#        "dasdjk tetete tetete tetete tetete")
seks = str(input())
temp_seks = seks.split(' ')
longest = max(temp_seks, key=len)
counter = collections.Counter(temp_seks)
most_common, occurencies = counter.most_common()[0]

print(most_common, longest)

#  end of task 22


