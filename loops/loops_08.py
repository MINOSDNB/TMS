'''
Ввести два целых числа a и b ( a < b ).
Вывести в порядке возрастания все целые числа,
расположенные между a и b (включая сами числа a и b ), а также количество n этих чисел.
'''


a1 = int(input('Enter number - '))
a2 = int(input('Enter number - '))

count = 0
for i in range(a1, a2 + 1):
    print(i)
    count += 1
print(f'Count = {count}')




