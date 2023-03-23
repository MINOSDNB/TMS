'''
Дано число.
Найти сумму и произведение его цифр.
'''


number = 123456789

list_of_number = list(str(number))
print(list_of_number)
result_sum = 0
result_n = 1
for i in list_of_number:
    result_sum += int(i)
    result_n *= int(i)
print(result_sum, result_n)


result_sum = 0
result_n = 1
while number:
    last_n = number % 10
    result_sum += last_n
    result_n *= last_n
    number //= 10
print(result_sum, result_n)

