'''
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы,
превосходящих среднее арифметическое значение элементов матрицы и сумма индексов которых четна.
'''


from random import randint

n = int(input('Enter number '))
m = int(input('Enter number '))

arr = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
print(arr)
count = 0
result_sum = 0
for arr_i in arr:
    for i in arr_i:
        result_sum += i
        count += 1

result_avg = result_sum / count

count = 0
for i, arr_i in enumerate(arr):
    for r, number in enumerate(arr_i):
        if (number > result_avg) and ((i + r) % 2) == 0:
            count += 1

print(count)


