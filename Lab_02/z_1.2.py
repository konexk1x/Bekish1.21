# Вариант 4
# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.
import random

random_list = []
for i in range(int(input("Введите размер списка random_list: "))):
    a = random.randint(0, 99)
    random_list.append(a)

p = 1
for j in range (0, len(random_list)):
    if j % 2 == 1:
        p *= random_list[j]

print("Элементы списка: " + str(random_list))
print("Произведение элементов списка с нечетными номерами: " + str(p))

max = random_list[0]
for k in range(0, len(random_list)):
    if random_list[k] > max:
        max = random_list[k]
        random_list.remove(max)

print("Наибольший элемент списка: " + str(max))
print("Новый список: " + str(random_list))
