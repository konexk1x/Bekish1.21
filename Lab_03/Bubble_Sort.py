nums=[1,2,6,4,7,5,3]

def BubbleSort(A): # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

BubbleSort(nums)
print(nums)
