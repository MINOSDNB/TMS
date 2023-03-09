"""
Ввести почтовый адрес. Проверить доменное имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика.
Иначе вывести надпись “DOMAIN NAME is not supported"
"""


a = str(input('Your email: '))
if '@gmail.com' in a:
    print(a)
else:
    print('DOMAIN NAME is not supported')

