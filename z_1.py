# В переменную Y ввести номер года. Определить, является ли год високосным.

Y = int(input("Введите год: "))
if Y%4 == 0:
    print("Год високосный")
else:
    print("Год не високосный")