def tribonacciGen(value):
    first_num = 0
    second_num = 0
    third_num = 1
    count = 0
    while count <= value:
        count += 1
        if count == 1 or count == 2:
            yield 0
        elif count == 3:
            yield 1
        else:
            num_sum = first_num + second_num + third_num
            first_num = second_num
            second_num = third_num
            third_num = num_sum
            yield num_sum


value = int(input("Введите количество чисел ряда Трибоначчи: "))
iter = tribonacciGen(value)

trib_row = []
for i in iter:
    trib_row.append(i)

print(trib_row)
