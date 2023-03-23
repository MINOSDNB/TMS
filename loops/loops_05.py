'''
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while
'''


n = int(input('Enter number - '))
result_sum = 0
i = 1
while i <= n:
    result_sum += i ** 3
    i += 1
print(result_sum)
