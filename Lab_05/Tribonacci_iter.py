class TribonacciIter:
    first_num = 0
    second_num = 0
    third_num = 1

    def __init__(self, value):
        self.count = 0
        self.limit = value

    def __next__(self):
        if self.count <= self.limit:
            self.count += 1
            if (self.count == 1 or self.count == 2):
                return self.first_num
            if (self.count == 3):
                return self.third_num
            else:
                num_sum = self.first_num + self.second_num + self.third_num
                self.first_num = self.second_num
                self.second_num = self.third_num
                self.third_num = num_sum
                return num_sum
        else:
            raise StopIteration

    def __iter__(self):
        return self


value = int(input("Введите количество чисел ряда Трибоначчи: : "))
iter = TribonacciIter(value)

trib_row = []
for i in iter:
    trib_row.append(i)
print(trib_row)
