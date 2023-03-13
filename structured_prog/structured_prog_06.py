my_str = input('Введте строку - ')
a1 = len(my_str)
if a1 > 10:
    print(my_str, '!!!')
elif a1 < 10:
    print(my_str[1])
else:
    print('Something wrong')
