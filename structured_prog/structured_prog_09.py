'''
Дан список целых чисел. Подсчитать сколько четных чисел в списке
'''


arr = [i for i in range(1, 10)]
print(arr)
count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print(f'count = {count}')

