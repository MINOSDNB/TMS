while True:
    sign = input('sign - ')
    if sign == '0':
        print('the end')
        break
    elif sign not in ('+', '-', '/', '*'):
        print('wrong sign, try again')
        continue
    x = int(input('x = '))
    y = int(input('y = '))
    if sign == '+':
        print(f'x + y = {x + y}')
    elif sign == '-':
        print(f'x - y = {x - y}')
    elif sign == '/':
        if y == 0:
            print('нельзя делить на ноль')
            continue
        print(f'x / y = {x / y}')
    elif sign == '*':
        print(f'x * y = {x * y}')

