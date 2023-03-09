arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
list_length = len(arr)
all_elements = 0
count = 0
while count < list_length:
    all_elements = all_elements + arr[count]
    count = count + 1
print(all_elements)

srd = all_elements / list_length
print(srd)






