'''
Написать игру. Пользователь должен угадать число. Сперва вводится диапазон угадывания.
После колличество попыток. В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку(больше или меньше искомое число).
Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.
'''


from random import randint

start = int(input('Start - '))
finish = int(input('Finish - '))
count = int(input('Count of attempts - '))
result = randint(start, finish)

while True:
    if count == 0:
        print(f'You are the loser и правильное число {result}')
        break
    attempt = int(input('Enter number - '))
    if attempt == result:
        print('You win')
    elif attempt < result:
        print('result > attempt')
    elif attempt > result:
        print('result < attempt')
    count -= 1

