'''
Создать список произвольного содержания.
После каждой операции выводить список на экран
Добавить к нему строку “Hello”.
Удалить первый элемент.
Поменять второй элемент на строку “World”.
Удалить элемент “World”
Вывести на экран перевернутый список
'''

my_list = [1, 2, 3, 4, 5, 6]
my_list.append("Hello!")
print(my_list)

my_list.remove(2)
print(my_list)

my_list[3] = "World"
print(my_list)

my_list.remove("World")
print(my_list)

print(my_list[::-1])
