result_sum = 0
while True:
    number = input('Enter number - ')
    if number == 'stop':
        print('The end')
        break
    result_sum += int(number)
    print(f'result sum = {result_sum}')


