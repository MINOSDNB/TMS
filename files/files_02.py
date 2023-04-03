# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.

with open('/users/ALEX/PycharmProjects/pythonProject/files/test_file_2.txt', 'a') as file:
    for _ in range(3):
        text = input('enter text ')
        text_2 = input('enter text 2 - ')
        file.writelines([f'{text}\n', text_2])
        file.write('\n')

print('--------------')

with open('/users/ALEX/PycharmProjects/pythonProject/files/test_file_2.txt') as file:
    print(file.read())
