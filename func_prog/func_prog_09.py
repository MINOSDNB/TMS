'''Дан список строк.
Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер строки в списке.
Использовать генератор списков.
'''

strings = ['hello', 'world', 'python']
formatted_strings = [f"{i} - {string}" for i, string in enumerate(strings)]
print(formatted_strings)
