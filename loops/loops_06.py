from random import randint

while True:
    number = randint(-9, 9)
    if number == 7:
        print('the end (number == 7) ')
        break
    print(number)
