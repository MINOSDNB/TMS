my_str = 'aadd vkmc pdkd'
print(" ".join(my_str.split()[::-1]))
my_list = my_str.split()
print(my_list)
my_list = my_list[::-1]
new_str = " ".join(my_list)
print(new_str)

