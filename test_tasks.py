#  1. Пользователь вводит 2 числа, создать список содержащий квадраты целых чисел между ними
#  2. Пользователь вводит целые числа, пока не введет слово end, поместить в список и вывести только нечетные
#  3. Пользователь вводит целые числа, пока не введет слово end, поместить в список и посчитать кол-во четных и нечетных
#  4. Список чисел, вывести все, которые больше предыдущего
#  5. Список чисел, поменять местами максимальный и минимальный элементы
#  6. Список чисел, определить различные элементы
#  7. Последовательность чисел - рост каждого, потом вводится рост Пети, нужно определить номер в списке, под которым
#  должен встать в строй Петя. если его рост равен чьему-то, то он встает последним после остальных
#  8. Дан список чисел, циклически сдвинуть его вправо, последний на место нулевого
from itertools import count

#  1 //
# print("task 1")
# print("Input a value")
# a = int(input())
# print("Input b value")
# b = int(input())
# list_kekov = []
#
# if a > b:
#     b+=1
#     while a > b:
#         #  val = b*b
#         list_kekov.append(b*b)
#         b+=1
# else:
#     a+=1
#     while b > a:
#         #  val = a*a
#         list_kekov.append(a*a)
#         a+=1
# print(list_kekov)
# print("end of task 1")

#  2 //
# print("task 2")
# list_kekov2 = []
# while True:
#     check = input()
#     if check == 'end':
#         break
#     else:
#         list_kekov2.append(int(check))
#
# for i in list_kekov2:
#     if i % 2 > 0:
#         print(i)
# print("end of task 2")

#  3 //
# print("task 3")
# list_kekov3 = []
# even = 0
# odd = 0
# while True:
#     check = input()
#     if check == 'end':
#         break
#     else:
#         list_kekov3.append(int(check))
#
# for i in list_kekov3:
#     if i % 2 == 0:
#         even += 1
#     if i % 2 > 0:
#         odd += 1
# print("Нечетные - " + str(even))
# print("Четные - " + str(odd))
# print("end of task 3")

#  4 //
# print("task 4")
# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])
# print("end of task 4")

#  5 //
# print("task 5")
# a = [int(i) for i in  input().split()]
# max_index = a.index(max(a))
# min_index = a.index(min(a))
# a[max_index], a[min_index] = a[min_index], a[max_index]
# print(a)
# print("end of task 5")

#  6 //
# print("task 6")
# initial_list = [int(i) for i in input().split()]
# unique = set(initial_list)
# print(len(unique))
# print("end of task 6")

#  7 //
# print("task 7")
# student_height = [int(i) for i in input().split()]
# student_height.sort()
# petya_height = int(input())
# for i in student_height:
#     if i < petya_height:
#         pass
#     elif i >= petya_height:
#         print("Место Пети в строю " + str(student_height.index(i) + 1))
#         break
# print("end of task 7")

#  8 //
print("task 8")
shift_list = [int(i) for i in input().split()]
for i in range(1):
    shift_list.insert(0, shift_list.pop())
# shift = 1
# shift_list = shift_list[-shift:] + shift_list[:-shift]
print(shift_list)
print("end of task 8")


