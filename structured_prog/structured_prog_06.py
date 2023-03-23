my_str = input('Введи строку - ')
if len(my_str) > 10:
    print(my_str, '!!!')
elif len(my_str) < 10:
    print(my_str[1])
else:
    print('Неправильно')


