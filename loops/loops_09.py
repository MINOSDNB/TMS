from random import randint


n = int(input('Enter number '))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(1, 9))
    print(arr_1)
    arr.append(arr_1)
print(arr)

