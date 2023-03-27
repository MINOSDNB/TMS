'''
Написать функцию, которая получает на вход имя и выводит строку вида: “Hello, {name}”.
Создать список из 5 имен.
Вызвать функцию для каждого элемента списка в цикле.
'''


def my_funct(name):
    print(f'Hello {name}')


def main():
    arr = ['Boris', 'Tony', 'Charlie', 'Tureckiy', 'Valera']
    for name in arr:
        my_funct(name)


if __name__ == '__main__':
    main()
