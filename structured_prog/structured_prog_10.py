my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(my_dict.keys())

for key in keys:
    new_key = key + str(len(key))
    my_dict[new_key] = my_dict.pop(key)

print(my_dict)


