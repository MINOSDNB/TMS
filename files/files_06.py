# with open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt", 'r') as file, \
#         open("/users/ALEX/PycharmProjects/pythonProject/files/file_1_1.txt", 'w') as file_1_1:
#     count = 0
#     while line_1 := file.readline():
#         line_2 = file_1_1.readline()
#         if line_1 != line_2:
#             print(f'differences in {count} line')
#             break
#         count += 1


with open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt", 'r') as file, \
         open("/users/ALEX/PycharmProjects/pythonProject/files/file_1_1.txt", 'r') as file_1_1:
    for index, (line_1, line_2) in enumerate(zip(file, file_1_1)):
        if line_1 != line_2:
            print(f'differences in {index + 1} line')
