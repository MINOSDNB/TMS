from random import randint


n = int(input('Enter number '))
m = int(input('Enter number '))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(m):
        arr_1.append(randint(0, 9))
    #print(arr_1)
    arr.append(arr_1)
print(arr)

count = 0
for arr_i in arr:
    for j in arr_i:
        if j == 7:
            count += 1
print(count)

