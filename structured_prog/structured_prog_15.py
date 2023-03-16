dict = {}
for number in range(200, 300):
    sum_d_number = 0
    for i in range(1, number):
        if number % i == 0:
            sum_d_number += i
    dict[number] = sum_d_number

for key in dict.keys():
    for value_key in dict.keys():
        if dict[key] == value_key and dict[value_key] == key:
            print(key, value_key)
