'''Задача:
Дан массив из целых чисел. Создать из них максимальное число, ставя их друг за другом.
Пример: [1, 3, 5, 29, 24, 71, 6] -> 715329241

link: https://leetcode.com/problems/largest-number/'''

from functools import cmp_to_key

numbers = [int(i) for i in input().split()]
print(numbers)

def length(number):
    length = 1
    while number // 10 > 0:
        length += 1
        number /= 10 
    return length

def comp(l, r):
    length_l = length(l)
    length_r = length(r)

    left_right = l * (10 ** length_r) + r
    right_left = r * (10 ** length_l) + l

    if left_right > right_left:
        return 1
    elif right_left > left_right:
        return -1
    else:
        return 0
    

numbers.sort(key=cmp_to_key(comp), reverse=True)
max_number = ''.join([str(i) for i in numbers])
print(max_number)