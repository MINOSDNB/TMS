"""
Ввести число, проверить на то, что было введено именно число.
Возвести его в куб и вывести результат на экран.
"""


a = input('Enter something: ')
if a.isdigit():
    a = int(a)
    result = a ** 3
    print(result)
else:
    print('a not number')


