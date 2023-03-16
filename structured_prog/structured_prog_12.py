arr = [1, 1]
for i in range(13):
    arr.append(arr[-1] + arr[-2])
print(arr, len(arr))


arr = [1, 1]
while len(arr) < 15:
    arr.append(arr[-1] + arr[-2])
print(arr, len(arr))

