a1 = int(input('Кол-во гостей '))
if a1 > 50:
    print('Ресторан')
elif a1 >= 20 and a1 <= 50:
    print('Кафе')
elif a1 < 20:
    print('Дом')
else:
    print('Something wrong')
