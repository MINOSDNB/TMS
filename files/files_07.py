# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл
import json
from random import randint

matrix = [[randint(1, 9)] for _ in range(5)]

with open('/users/ALEX/PycharmProjects/pythonProject/files/json_1.json') as file:
    data = json.dumps(matrix)
    print(type(data), data)
    file.write(data)


with open('/users/ALEX/PycharmProjects/pythonProject/files/json_1.json', 'r') as file, \
        open('/users/ALEX/PycharmProjects/pythonProject/files/json_.json', 'w') as file_2:
        data = json.load(file)
        for index_row, row in enumerate(data):
            for index_number, number in enumerate(row):
                if number % 2 == 0:
                    data[index_row][index_number] = 0
        print(type(data), data)

#   json.dump(data, file_2)

