'''
Рассчитать месячные выплаты (m) и суммарную выплату (s) по кредиту.
О кредите известно, что он составляет n рублей, берется на y лет, под p процентов.
n, y, p - вводятся с клавиатуры.
Месячные выплаты находятся по формуле:
m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)), где p выражается в долях единицы, а не процентах.
Суммарная выплата представляет собой выплаты за все месяцы каждого года:
s = (m * 12) * y
'''


n = input('Руб ')
y = input('Лет ')
p = input('Процент ')
n = float(n)
y = int(y)
p = float(p)
m = ((n * (p / 100)) * ((1 + (p / 100)) ** y) / (12 * (((1 + (p / 100)) ** y) - 1)))
s = ((m * 12) * y)
print('Месячные выплаты', m, 'Суммарная выплата', s)
