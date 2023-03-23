'''
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все четные по значению элементы.
'''


from random import randint

arr = [randint(1, 20) for _ in range(19)]
print(arr, len(arr))

max_number = max(arr)
print(max_number)
print(f'min - {min(arr)}')


max_number_oun_solution = arr[0]
for i in arr:
    if i > max_number_oun_solution:
        max_number_oun_solution = i
print(f'max_number_oun_solution = {max_number_oun_solution}')

for index, number in enumerate(arr):
    if number % 2 == 0:
        arr[index] = max_number
print(arr)





