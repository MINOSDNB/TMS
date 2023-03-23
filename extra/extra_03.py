arr = [8, 7, 3, 4, 4, 4, 5, 5, 2]

for i in range(len(arr)):
    for j in range(i, len(arr)):
       if arr[i] > arr[j]:
           arr[i], arr[j] = arr[j], arr[i]

print(arr)
