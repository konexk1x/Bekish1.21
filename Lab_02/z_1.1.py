# Вариант 2
# Введите одномерный целочисленный список.
# Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

list = []
for i in range(int(input("Введите размер списка list: "))):
    list.append(int(input("Введите элемент №" + str(i + 1) + ": ")))

    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max and list[i] % 2 == 1:
            max = list[i]

    min_abs = abs(list[0])
    for i in range(1, len(list)):
        if abs(list[i]) < min_abs:
            min_abs = abs(list[i])

print("Элементы списка: " + str(list))
print("Максимальный нечетный элемень в списке: " + str(max))
print("Максимальный по модулю элемент в списке: " + str(min_abs))
