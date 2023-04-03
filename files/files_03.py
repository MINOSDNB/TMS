with open('/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt', 'a') as file:
    for _ in range(2):
        text = input('enter text - ')
        file.writelines([f'{text}\n'])
        file.write('\n')

print('------------')

with open('/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt') as file:
    print(file.read())
