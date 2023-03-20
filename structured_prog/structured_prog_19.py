from random import randint

matrix = [[randint(0, 9) for _ in range(4)] for _ in range(4)]

for arr in matrix:
    print(arr)

for index, arr in enumerate(matrix):
    max_element = max(arr)
    index_max_element = arr.index(max_element)
    arr[index], arr[index_max_element] = arr[index_max_element], arr[index]

print('after replace')
for arr in matrix:
    print(arr)

