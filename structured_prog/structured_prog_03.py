den = int(input('Введите рубли '))
den_1 = int(input('Введите копейки '))
if den > 0 and den_1 > 0:
    print(den, 'рублей', den_1, 'копеек')
elif den == 0 and den_1 > 0:
    print(den_1, 'копеек')
else:
    print(den, 'рублей')
