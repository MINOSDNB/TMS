with open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt", 'r') as file, \
        open("/users/ALEX/PycharmProjects/pythonProject/files/file_1_1.txt", 'w') as file_1_1, \
        open("/users/ALEX/PycharmProjects/pythonProject/files/file_1_2.txt", 'w') as file_1_2:
    data = file.readlines()
    data_for_1_1 = data[::2]
    data_for_1_2 = data[1::2]
    file_1_1.writelines(data_for_1_1)
    file_1_2.writelines(data_for_1_2)

