'''
Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а
'''


arr = ['Britva', 'Turecki', 'Pevcaya']

for vamilia in arr:
    if vamilia[0] == 'P' and vamilia[-1] == 'a':
        print(vamilia)
