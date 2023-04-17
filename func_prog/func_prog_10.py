'''
Создать lambda функцию, которая принимает на вход неопределенное количество именованных аргументов
и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
'''

lam_func = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(lam_func(abc=5, oiu=6))
