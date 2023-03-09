'''
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
'''


my_string = input()
result = my_string.split(' ')
result.reverse()
st = ' '.join(result)
print(st)
