# Задание 2. Задачи на многомерные списки
# 1. В матрице найти номер строки, сумма чисел в которой максимальна.

import random

import numpy as np

row = int(input("Введите количество строк матрицы: "))
col = int(input("Введите количество столбцов матрицы: "))
matrix = np.array([[random.randint(0, 30) for j in range(col)] for i in range(row)])

print("Случайная матрица: \n" + str(matrix))

for i in range(row):
    row_sum = 0
    for j in range(col):
        row_sum += matrix[i][j]
    print("Сумма чисел в строке №" + str(i+1) + ": ", row_sum)

max_row_sum = 0
row_index = 0
if row_sum > max_row_sum:
    max_row_sum = row_sum
    row_index = i
print("Номер строки с максимальной суммой чисел: ", row_index + 1)
