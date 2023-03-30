strings = str(i * i for i in range(1))
formatted_strings = [f"{i} - {string}" for i, string in enumerate(strings)]
print(formatted_strings)
