arr = [i for i in range(1, 9)]
print(arr)

arr_new = []
while len(arr) > 1:
    arr_new.append(arr.pop(1))
arr_new.append(arr.pop(0))
print(arr_new)

arr = [i for i in range(1, 9)]
print(arr)
arr_new_2 = []
for i in range(1, len(arr)):
    arr_new_2.append(arr[i])
arr_new_2.append(arr[0])
print(arr_new_2)
