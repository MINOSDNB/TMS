'''
Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
Также, если эта центральная буква равна первой букве в строке,
то создать и вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
Для создания результирующий строки используйте срез)
'''


my_str = input('enter str - ')
midle_str = my_str[len(my_str) // 2]
print(midle_str)
if midle_str == my_str[0]:
    new_str = my_str[1:-1]
    print(new_str)
    


