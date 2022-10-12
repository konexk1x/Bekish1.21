# Трибоначчи

def tribonacci(a):
    global num
    if a == 0 or a == 1:
        num = 0
    elif a == 2 or a == 3:
        num = 1
    elif a > 3:
        num = tribonacci(a-1) + tribonacci(a-2) + tribonacci(a-3)
    return num

row_length = int(input("Укажите длину ряда чисел Трибоначчи: "))
number = tribonacci(row_length)
trib_row = []
for i in range(row_length):
    trib_row.append(tribonacci(i))
print("Последовательность чисел Трибоначчи из " + str(row_length) + " элементов", trib_row)

