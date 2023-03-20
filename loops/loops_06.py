'''
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
'''


from random import randint

while True:
    number = randint(-9, 9)
    if number == 7:
        print('the end (number == 7) ')
        break
    print(number)
