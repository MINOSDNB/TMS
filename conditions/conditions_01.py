"""
Ввести предложение.
Если число символов в предложении кратно 3 - добавить ! к концу строки.
Вывести строку на экран в любом случае
"""


a = str(input())
if (len(a) % 3) == 0:
    a = a + '!'
    print(a)
if (len(a) % 3) != 0:
    print(a)
