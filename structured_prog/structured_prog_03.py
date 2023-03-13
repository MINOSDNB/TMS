a1 = int(input('Рубли - '))
a2 = int(input('Копейки - '))
if a1 > 0 and a2 > 0:
    print(a1, 'рублей', a2, 'копеек')
elif a1 <= 0 and a2 > 0:
    print(a2, 'копеек')
elif a1 > 0 and a2 <=0:
    print(a1, 'рублей')
else:
    print('Something wrong')
