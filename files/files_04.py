with open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_1.txt", "r") as input_file:
    lines = input_file.readlines()

with open("/users/ALEX/PycharmProjects/pythonProject/files/test_file_2.txt", "w") as output_file:
    for line in lines:
        new_line = line.translate(str.maketrans("01", "10"))
        output_file.write(new_line)
print(output_file)

