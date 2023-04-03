with open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt", 'r') as file, \
        open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_11.txt", "w") as file_new:
    fileread = file.read()
    for i in fileread:
        if i == '0':
            i = '1'
        elif i == '1':
            i = '0'
