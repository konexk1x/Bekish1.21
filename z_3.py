# Найти значение минимального элемента списка.

import  random

n = int(input("Введите размер списка: "))
A = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)

print("Элементы списка: " + str(A))
min = A[0]

for i in range(1, len(A)):
    if A[i] < min:
        min = A[i]
print("Минимальное значение в списке: " + str(min))