# Задача на рекурсию
# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем
# сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

def square(x, y):
    if x == y:
        count = 1
        print("Квадрат со стороной " + str(x) + " - " + str(count) + "-й")
    else:
        count = square(max(x, y) - min(x, y), min(x, y)) + 1
        print("Квадрат со стороной " + str(min(x, y)) + " - " + str(count) + "-й")
    return count


a = int(input('Введите длину прямоугольника a: '))
b = int(input('Введите ширину прямоугольника b: '))

print("Прямоугольник размерами " + str(a) + "х" + str(b) +
      " можно нарезать на " + str(square(a, b)) + " квадрата(ов)")
