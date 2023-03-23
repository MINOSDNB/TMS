'''
Ввести строку с клавиатуры.
Вернуть результат логического выражения: длина строки не меньше 8 или в строке есть “python”.
'''


a = input('Введите строку - ')
str_1 = len(a)
if str_1 >= 8 or 'python' in a:
    print(a)
else:
    print('Something wrong')

