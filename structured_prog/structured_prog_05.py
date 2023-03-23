number = int(input('Кол-во гостей = '))
if number > 50:
    print('Ресторан')
elif (number >= 20) and (number < 50):
    print('Кафе')
else:
    print('Дома')


